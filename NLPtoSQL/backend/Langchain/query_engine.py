# LangChain imports for building NLP to SQL conversion pipeline
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import json
import os
import re
from enum import Enum
from collections import deque
from datetime import datetime
from typing import List, Dict, Optional

# Define what type of question user is asking
class QueryIntent(Enum):
    SQL_QUERY = "sql_query"
    SQL_SPATIAL = "sql_spatial"          # NEW: spatial/geo queries with geometry
    CASUAL_CHAT = "casual_chat"
    GENERAL_KNOWLEDGE = "general_knowledge"
    SARCASTIC_RESPONSE = "sarcastic_response"
    AMBIGUOUS = "ambiguous"

class ConversationMemory:
    """Manages conversation history with smart token optimization"""
    
    def __init__(self, max_exchanges: int = 5, max_tokens_per_msg: int = 500):
        self.max_exchanges = max_exchanges
        self.max_tokens_per_msg = max_tokens_per_msg
        self.messages = deque(maxlen=max_exchanges * 2)  # Store last N exchanges (user + AI pairs)
        self.session_id = None
        self.created_at = datetime.now()
        
    def add_message(self, role: str, content: str, metadata: Dict = None):
        """Add a message to conversation history"""
        # Truncate very long messages
        if len(content) > self.max_tokens_per_msg * 4:  # Approx 4 chars per token
            content = content[:self.max_tokens_per_msg * 4] + "... [truncated]"
        
        msg_data = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        
        self.messages.append(msg_data)
    
    def get_langchain_messages(self) -> List:
        """Convert stored messages to LangChain message format"""
        lc_messages = []
        
        for msg in self.messages:
            if msg["role"] == "user":
                lc_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                lc_messages.append(AIMessage(content=msg["content"]))
        
        return lc_messages
    
    def get_context_summary(self) -> str:
        """Generate a compact summary of recent conversation for context"""
        if len(self.messages) == 0:
            return ""
        
        summary_parts = []
        for msg in list(self.messages)[-6:]:  # Last 3 exchanges
            role = "User" if msg["role"] == "user" else "Assistant"
            content = msg["content"][:200]  # First 200 chars
            summary_parts.append(f"{role}: {content}")
        
        return "\n".join(summary_parts)
    
    def clear(self):
        """Clear conversation history"""
        self.messages.clear()
    
    def get_token_estimate(self) -> int:
        """Estimate total tokens in conversation history"""
        total_chars = sum(len(msg["content"]) for msg in self.messages)
        return total_chars // 4  # Rough estimate: 4 chars ≈ 1 token
    
    def to_dict(self) -> Dict:
        """Export conversation history"""
        return {
            "session_id": self.session_id,
            "created_at": self.created_at.isoformat(),
            "message_count": len(self.messages),
            "messages": list(self.messages),
            "token_estimate": self.get_token_estimate()
        }
    
    def from_dict(self, data: Dict):
        """Import conversation history"""
        self.session_id = data.get("session_id")
        self.created_at = datetime.fromisoformat(data.get("created_at", datetime.now().isoformat()))
        self.messages.clear()
        for msg in data.get("messages", [])[-self.max_exchanges * 2:]:
            self.messages.append(msg)

class QueryEngine:
    """Main engine: converts natural language to SQL with intent detection and memory"""
    
    def __init__(self, db: SQLDatabase, db_description: str = None, table_descriptions: Dict = None, selected_tables: list = None, session_id: str = None, stored_schema: Dict = None):
        self.db = db
        self.db_description = db_description or "database"
        self.table_descriptions = table_descriptions or {}
        self.selected_tables = selected_tables or []
        self.stored_schema = stored_schema or {}  # Use stored schema if available
        
        # Initialize conversation memory
        self.memory = ConversationMemory(max_exchanges=5, max_tokens_per_msg=500)
        self.memory.session_id = session_id or f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Setup Groq LLM
        self.llm = ChatGroq(
            temperature=0,
            model_name="llama-3.3-70b-versatile"
        )
        
        # Setup web search tool
        # Setup web search tool
        try:
            from langchain_community.tools import DuckDuckGoSearchRun
            self.search_tool = DuckDuckGoSearchRun()
        except ImportError:
            print("WARNING: DuckDuckGoSearchRun (ddgs) not found. Web search disabled.")
            self.search_tool = None
        except Exception as e:
            print(f"WARNING: Web search tool init failed: {e}")
            self.search_tool = None
        
        # Create all AI prompts
        self._setup_chains()
    
    def get_geometry_columns(self) -> str:
        """
        Auto-discover geometry/geography columns from the database schema.
        Returns a string describing which tables have geometry columns and their column names.
        Only SELECT queries will be allowed — this is read-only.
        """
        try:
            # Query information_schema to find USER-DEFINED columns (geometry/geography in PostGIS)
            query = """
                SELECT table_name, column_name, udt_name
                FROM information_schema.columns
                WHERE data_type = 'USER-DEFINED'
                AND table_schema = 'public'
                ORDER BY table_name, column_name
            """
            from sqlalchemy import text
            with self.db._engine.connect() as conn:
                rows = conn.execute(text(query)).fetchall()

            if not rows:
                return "No geometry columns found in this database."

            geo_schema_lines = ["Geometry columns found in the database:"]
            for row in rows:
                geo_schema_lines.append(
                    f"  - Table: '{row[0]}', Column: '{row[1]}', Type: '{row[2]}'"
                )
            return "\n".join(geo_schema_lines)

        except Exception as e:
            print(f"WARNING: Could not auto-discover geometry columns: {e}")
            # Fallback: use hardcoded known geometry column for main_farm
            return "Geometry columns (fallback): Table 'main_farm', Column 'polygon' (USER-DEFINED/geometry type)"


    def _build_domain_description(self):
        """Build domain description from table descriptions and selected tables"""
        if not self.table_descriptions:
            return "A financial services database"
        
        desc_parts = [f"Database: {self.db_description}"]
        desc_parts.append("\nSelected Tables:") 
        
        for table_name in self.selected_tables:
            if table_name in self.table_descriptions:
                table_info = self.table_descriptions[table_name]
                desc = table_info.get('description', 'No description') if isinstance(table_info, dict) else str(table_info)
                desc_parts.append(f"- {table_name}: {desc}")
        
        return "\n".join(desc_parts)
    
    def get_filtered_schema(self, table_names: List[str] = None) -> str:
        """Get schema for specific tables only"""
        if not table_names:
            table_names = self.selected_tables
        
        # Use stored schema if available
        if self.stored_schema:
            filtered_schema = {}
            for table in table_names:
                if table in self.stored_schema:
                    filtered_schema[table] = self.stored_schema[table]
            
            if filtered_schema:
                schema_parts = []
                for table_name, columns in filtered_schema.items():
                    schema_parts.append(f"\nTable: {table_name}")
                    for col in columns:
                        schema_parts.append(f"  - {col['column']}: {col['type']}")
                return "\n".join(schema_parts)
        
        # Fallback to database schema if stored schema not available
        try:
            all_tables = self.db.get_usable_table_names()
            available_tables = [t for t in table_names if t in all_tables or t.split('.')[-1] in all_tables]
            
            if available_tables:
                return self.db.get_table_info(table_names=available_tables)
            else:
                return "No matching tables found in database"
        except Exception as e:
            return f"Error getting schema: {str(e)}"
    
    def _setup_chains(self):
        """Create AI prompts with conversation memory support"""
        
        # 1. Intent Detection with Memory Context
        db_domain_desc = self._build_domain_description()
        self.intent_prompt = ChatPromptTemplate.from_messages([
            ("system", f"""You are an Intent Classification Engine for a {self.db_description}.
            Your ONLY task is to classify whether a user question is related to our DATABASE or NOT.

            DATABASE DESCRIPTION:
            {db_domain_desc}

            INTENT CATEGORIES (CHOOSE EXACTLY ONE):
            1. SQL_QUERY - Questions about database tables and data (no map/location/geometry involved)
            2. SQL_SPATIAL - Questions involving location, geometry, maps, coordinates, spatial relationships.
               Examples: "farms near this point", "inside this polygon", "intersects with this shape",
               "within 10km", "farms that touch this boundary", any question that comes with GeoJSON/geometry data.
            3. CASUAL_CHAT - Greetings, small talk: "Hi", "How are you?", "Tell me a joke?"
            4. GENERAL_KNOWLEDGE - Unrelated to database: "Who is PM of India?", "What is AI?", "Explain photosynthesis"
            5. SARCASTIC_RESPONSE - Troll, nonsense questions not related to our database
            6. AMBIGUOUS - Not clear enough: "Show me the thing", "Give me the list"

            OUTPUT RULE: Return ONLY ONE word: SQL_QUERY, SQL_SPATIAL, CASUAL_CHAT, GENERAL_KNOWLEDGE, SARCASTIC_RESPONSE, or AMBIGUOUS
            No explanation. No extra words.

            IMPORTANT: If the user's question contains any GeoJSON geometry, spatial words (near, within, inside,
            intersects, buffer, radius, polygon, point, coordinates), classify it as SQL_SPATIAL.

            Conversation context: {{conversation_context}}"""),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", "{question}")
        ])
        
        self.intent_chain = self.intent_prompt | self.llm | StrOutputParser()
        
        # 2. SQL Generation with Conversation Context
        self.query_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert SQL query generator for a financial services database.

            Schema: {schema}

            SELECTED TABLES ONLY - USE ONLY THESE TABLES:
            {selected_tables_list}

            CRITICAL: You can ONLY query tables from the selected tables list above. 
            If a user asks about data not in these tables, respond with:
            "I can only query data from the selected tables: [list the selected tables]"

            Recent Conversation Context:
            {conversation_context}

            🚨🚨🚨 ABSOLUTE CRITICAL WARNING - READ-ONLY DATABASE 🚨🚨🚨
            ⛔ YOU ARE STRICTLY FORBIDDEN TO GENERATE ANY QUERIES THAT MODIFY DATA ⛔

            PROHIBITED OPERATIONS - NEVER GENERATE THESE:
            ❌ UPDATE - Modifies existing data
            ❌ DELETE - Removes data
            ❌ INSERT - Adds new data
            ❌ DROP - Deletes tables/databases
            ❌ TRUNCATE - Removes all rows
            ❌ ALTER - Changes table structure
            ❌ CREATE - Creates new objects
            ❌ RENAME - Renames objects
            ❌ REPLACE - Replaces data
            ❌ MERGE - Merges data
            ❌ COMMIT - Commits transactions
            ❌ ROLLBACK - Rolls back transactions
            ❌ SAVEPOINT - Creates savepoints
            ❌ GRANT - Modifies permissions
            ❌ REVOKE - Removes permissions

            ONLY ALLOWED: SELECT queries for reading data

            If user asks to modify/delete/update/insert data, respond with:
            "I can only generate SELECT queries to read data. I cannot modify the database."

            CRITICAL FROM/JOIN CLAUSE RULES - READ CAREFULLY:
            ❌ NEVER WRITE: FROM crm_customer crm_customer.c
            ❌ NEVER WRITE: FROM table_name table_name.alias
            ✅ ALWAYS WRITE: FROM crm_customer c
            ✅ ALWAYS WRITE: FROM table_name alias

            The alias comes DIRECTLY after table name with just a SPACE, NO DOT!

            CRITICAL COLUMN QUALIFICATION RULES:
            1. If table has alias: Use ONLY alias.column (e.g., "c.id" NOT "c.crm_customer.id")
            2. If no alias: Use table.column (e.g., "crm_customer.id")
            3. NEVER use table.alias.column format - THIS IS INVALID SYNTAX
            4. NEVER use alias.table.column format - THIS IS INVALID SYNTAX
            5. When using COUNT/SUM/AVG: COUNT(alias.column) NOT COUNT(table.alias.column)

            Complete Examples:
            ✅ CORRECT:
            - SELECT c.* FROM crm_customer c WHERE c.city = 'Mumbai'
            - SELECT c.id, c.name FROM crm_customer c
            - SELECT COUNT(c.id) FROM crm_customer c
            - SELECT t.title FROM tasks t JOIN crm_customer c ON t.customer_id = c.id

            ❌ ABSOLUTELY WRONG - NEVER DO THIS:
            - FROM crm_customer crm_customer.c (INVALID SYNTAX!)
            - FROM tasks tasks.t (INVALID SYNTAX!)
            - SELECT c.crm_customer.id (INVALID SYNTAX!)
            - SELECT crm_customer.c.id (INVALID SYNTAX!)

            POSTGRESQL INFORMATION_SCHEMA RULES:
            1. information_schema.referential_constraints columns: constraint_name, constraint_schema, unique_constraint_name
            2. information_schema.table_constraints columns: constraint_name, table_schema, table_name, constraint_type
            3. information_schema.key_column_usage columns: constraint_name, table_name, column_name
            4. To find related tables via foreign keys:
            ✅ CORRECT:
            SELECT kcu.table_name 
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu ON tc.constraint_name = kcu.constraint_name
            WHERE tc.constraint_type = 'FOREIGN KEY'
            
            ❌ WRONG: SELECT rc.table_name FROM information_schema.referential_constraints rc (table_name doesn't exist!)

            OTHER RULES:
            1. Generate ONLY ONE SQL statement
            2. SUBQUERY RULES - CRITICAL:
            ❌ NEVER: (SELECT * FROM cte_name) - Returns multiple columns, INVALID!
            ❌ NEVER: (SELECT col1, col2 FROM table) - Returns multiple columns, INVALID!
            ✅ ALWAYS use json_agg for multi-row/multi-column results:
                (SELECT json_agg(row_to_json(t)) FROM (SELECT * FROM cte_name) t)
                (SELECT json_agg(json_build_object('id', id, 'name', name)) FROM table)
            ✅ For single column: (SELECT array_agg(column) FROM table)
            3. Use CTEs (WITH clauses) for complex queries
            4. Consider conversation context for pronoun resolution
            5. Each subquery in SELECT clause must return EXACTLY ONE column and ONE row

            Return ONLY the SQL query without explanations."""),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", "Generate SQL for: {question}")
        ])
        
        self.query_chain = self.query_prompt | self.llm | StrOutputParser()
        
        # 3. Table Selection Chain
        self.table_prompt = ChatPromptTemplate.from_messages([
            ("system", """Return ONLY a JSON array of relevant table names.

Tables: {table_details}

Recent context: {conversation_context}

Return format: ["TableName1", "TableName2"]"""),
            ("human", "{question}")
        ])
        
        self.table_chain = self.table_prompt | self.llm | StrOutputParser()
        
        # 4. Sarcastic Response Chain
        db_topics = self._extract_database_topics()
        self.sarcastic_prompt = ChatPromptTemplate.from_messages([
            ("system", f"""You are a witty AI assistant for a {self.db_description}.

            The user asked something NOT related to our database.

            Respond with ONE SHORT sarcastic line (max 1 sentence):
            - Be funny but professional
            - Mention database topics: {db_topics}
            - Do NOT suggest other topics"""),
                        ("human", "{question}")
                    ])
        
        self.sarcastic_chain = self.sarcastic_prompt | self.llm | StrOutputParser()
        
        # 5. SQL Error Correction Chain
        self.sql_fix_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a SQL error correction expert.

        Schema: {schema}

        Failed SQL Query:
        {failed_query}

        Error Message:
        {error_message}

        Your task: Fix the SQL query based on the error.

        🚨 CRITICAL: ONLY FIX SELECT QUERIES - NEVER GENERATE UPDATE/DELETE/INSERT/DROP/TRUNCATE/ALTER 🚨

        COMMON FIXES:
        1. Column doesn't exist → Check schema for correct column name
        2. Table doesn't exist → Use correct table name from schema
        3. Subquery returns multiple columns → Wrap with json_agg(row_to_json(t))
        4. Syntax error → Fix JOIN, WHERE, or alias issues
        5. Invalid reference → Fix table.alias.column to alias.column

        Return ONLY the corrected SELECT query, no explanations."""),
                    ("human", "Fix this query")
                ])
        
        self.sql_fix_chain = self.sql_fix_prompt | self.llm | StrOutputParser()
    
    def classify_intent(self, question: str) -> tuple:
        """Determine question type with conversation context"""
        token_usage = {}
        try:
            context = self.memory.get_context_summary()
            chat_history = self.memory.get_langchain_messages()
            
            intent_response_obj = (self.intent_prompt | self.llm).invoke({
                "question": question,
                "conversation_context": context,
                "chat_history": chat_history[-4:] if chat_history else []
            })
            
            # Extract token usage from response metadata
            if hasattr(intent_response_obj, 'response_metadata'):
                usage = intent_response_obj.response_metadata.get('token_usage', {})
                token_usage = {
                    "prompt_tokens": usage.get('prompt_tokens', 0),
                    "completion_tokens": usage.get('completion_tokens', 0),
                    "total_tokens": usage.get('total_tokens', 0)
                }
            
            intent_str = intent_response_obj.content.strip().upper()
            print(f"Intent classification: {intent_str}")
            
            # Check SQL_SPATIAL BEFORE SQL_QUERY (since SQL_SPATIAL contains "SQL")
            if "SQL_SPATIAL" in intent_str:
                return QueryIntent.SQL_SPATIAL, token_usage
            elif "SQL_QUERY" in intent_str:
                return QueryIntent.SQL_QUERY, token_usage
            elif "CASUAL_CHAT" in intent_str:
                return QueryIntent.CASUAL_CHAT, token_usage
            elif "GENERAL_KNOWLEDGE" in intent_str:
                return QueryIntent.GENERAL_KNOWLEDGE, token_usage
            elif "SARCASTIC" in intent_str:
                return QueryIntent.SARCASTIC_RESPONSE, token_usage
            else:
                return QueryIntent.AMBIGUOUS, token_usage
                
        except Exception as e:
            print(f"Intent classification error: {e}")
            return QueryIntent.AMBIGUOUS, token_usage
    
    def _rephrase_search_results(self, question: str, search_results: str) -> str:
        """Summarize web search results"""
        try:
            rephrase_prompt = ChatPromptTemplate.from_messages([
                ("system", """Summarize search results into 2-3 sentences.
                Keep only relevant information. Be concise and factual."""),
                ("human", f"Question: {question}\n\nSearch results: {search_results}")
            ])
            rephrase_chain = rephrase_prompt | self.llm | StrOutputParser()
            return rephrase_chain.invoke({})
        except Exception as e:
            return search_results[:200] + "..." if len(search_results) > 200 else search_results
    
    def handle_casual_chat(self, question: str):
        """Handle casual chat questions with LLM"""
        try:
            chat_prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a friendly AI assistant. Answer casual questions naturally and conversationally. Keep responses brief (1-2 sentences)."),
                ("human", "{question}")
            ])
            chat_chain = chat_prompt | self.llm | StrOutputParser()
            response = chat_chain.invoke({"question": question})
            
            return {
                "intent": "casual_chat",
                "response": response
            }
        except Exception as e:
            return {
                "intent": "casual_chat",
                "response": "Hey! I'm here to help. What would you like to know?",
                "error": str(e)
            }
    
    def handle_general_knowledge(self, question: str):
        """Handle general knowledge questions with web search"""
        if not self.search_tool:
            return {
                "intent": "general_knowledge",
                "response": "I'm sorry, I cannot browse the web right now because the search tool is unavailable. I can only answer database questions."
            }

        try:
            print(f"Performing web search for: {question}")
            search_results = self.search_tool.run(question)
            rephrased = self._rephrase_search_results(question, search_results)
            
            return {
                "intent": "general_knowledge",
                "response": rephrased
            }
            
        except Exception as e:
            return {
                "intent": "general_knowledge",
                "response": f"I'd need to search the web for that, but I'm primarily designed for financial database queries.",
                "error": str(e)
            }
    
    def handle_sarcastic_response(self, question: str):
        """Generate witty response for irrelevant questions"""
        try:
            sarcastic_response = self.sarcastic_chain.invoke({"question": question})
            return {
                "intent": "sarcastic_response",
                "response": sarcastic_response
            }
        except Exception as e:
            return {
                "intent": "sarcastic_response",
                "response": "Nice try! I only know about customers, transactions, insurance, risk profiles, tasks, and employees."
            }
    
    def _extract_database_topics(self) -> str:
        """Extract main topics from table names"""
        if not self.table_descriptions:
            return "data"
        
        topics = list(self.table_descriptions.keys())
        return ", ".join(topics[:5])  # First 5 tables
    
    def get_table_details(self):
        """Get table descriptions from metadata"""
        if not self.table_descriptions:
            return "No table descriptions available"
        
        # Filter by selected_tables if provided
        tables_to_use = self.table_descriptions
        if self.selected_tables:
            tables_to_use = {k: v for k, v in self.table_descriptions.items() if k in self.selected_tables}
        
        details = ""
        for table_name, description in tables_to_use.items():
            details += f"Table: {table_name}\nDescription: {description}\n\n"
        
        return details
    
    def get_filtered_schema(self, table_names):
        """Get schema for specific tables only"""
        if not table_names:
            # If selected_tables is set, use only those
            if self.selected_tables:
                return self._get_schema_for_tables(self.selected_tables)
            return self.db.table_info
        
        try:
            all_tables = self.db.get_usable_table_names()
            matched_tables = []
            normalized_selected = {t.split('.')[-1].lower() for t in self.selected_tables} if self.selected_tables else set()
            
            for actual_table in all_tables:
                for req_name in table_names:
                    if (req_name.lower() in actual_table.lower() or 
                        actual_table.lower() in req_name.lower()):
                        # If selected_tables is set, only include if in selected_tables
                        if not self.selected_tables or actual_table.lower() in normalized_selected:
                            matched_tables.append(actual_table)
                            print(f"Matched table: {req_name} -> {actual_table}")
                        break
            
            if matched_tables:
                return self._get_schema_for_tables(matched_tables)
            
        except Exception as e:
            print(f"Schema filtering failed: {e}")
        
        return self.db.table_info
    
    def _get_schema_for_tables(self, tables: list) -> str:
        """Helper to get schema for specific tables"""
        try:
            all_tables = set(self.db.get_usable_table_names())
            normalized_tables = []
            for table in tables:
                table_name = table.split('.')[-1]
                if table_name in all_tables:
                    normalized_tables.append(table_name)

            normalized_tables = list(dict.fromkeys(normalized_tables))
            if not normalized_tables:
                return "Schema unavailable for requested tables"

            filtered_db = SQLDatabase.from_uri(
                self.db._engine.url,
                sample_rows_in_table_info=0,
                include_tables=normalized_tables,
                engine_args={"pool_pre_ping": True, "pool_recycle": 300}
            )
            return filtered_db.table_info
        except Exception as e:
            print(f"Failed to get schema for tables {tables}: {e}")
            try:
                fallback_tables = [t.split('.')[-1] for t in tables]
                fallback_tables = list(dict.fromkeys(fallback_tables))
                return self.db.get_table_info(table_names=fallback_tables)
            except Exception:
                return "Schema unavailable for requested tables"
    
    def validate_and_fix_sql(self, sql_query: str, schema: str = "") -> str:
        """Validate and fix SQL query"""
        if "(SELECT *" in sql_query:
            print("Warning: Found SELECT * in subquery context")
        
        # Fix double qualification: table.alias.column → alias.column
        # Pattern 1: crm_customer.c.id → c.id
        sql_query = re.sub(
            r'\b(\w+)\.([a-z])\.(\w+)\b',
            r'\2.\3',
            sql_query,
            flags=re.IGNORECASE
        )
        
        # Pattern 2: alias.table.column → alias.column
        sql_query = re.sub(
            r'\b([a-z])\.(\w+)\.(\w+)\b',
            r'\1.\3',
            sql_query,
            flags=re.IGNORECASE
        )
        
        # Pattern 3: table.table.column → table.column
        sql_query = re.sub(
            r'\b(\w+)\.(\1)\.(\w+)\b',
            r'\1.\3',
            sql_query,
            flags=re.IGNORECASE
        )
        
        print(f"SQL after qualification fix: {sql_query}")
        
        if schema:
            col_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s+'
            actual_cols = re.findall(col_pattern, schema)
            col_map = {col.lower(): col for col in actual_cols}
            
            for lower_col, actual_col in col_map.items():
                pattern = r'\b' + lower_col + r'\b'
                sql_query = re.sub(pattern, actual_col, sql_query, flags=re.IGNORECASE)
        
        return sql_query

    def _extract_executable_sql(self, llm_content: str) -> str:
        """Extract a single executable PostgreSQL SELECT/WITH statement from raw LLM text."""
        if not llm_content:
            return ""

        content = llm_content.replace("```sql", "").replace("```", "").strip()

        # Keep only content starting from first SQL keyword
        start_match = re.search(r"\b(WITH|SELECT)\b", content, flags=re.IGNORECASE)
        if start_match:
            content = content[start_match.start():]

        # Remove obvious non-SQL trailers
        trailer_patterns = [
            r"\n\s*Note\s*:",
            r"\n\s*Explanation\s*:",
            r"\n\s*This query",
            r"\n\s*The query",
            r"\n\s*Output",
        ]
        for pattern in trailer_patterns:
            match = re.search(pattern, content, flags=re.IGNORECASE)
            if match:
                content = content[:match.start()]
                break

        # Keep only first SQL statement if multiple are present
        first_semicolon = content.find(';')
        if first_semicolon != -1:
            content = content[:first_semicolon + 1]

        # Normalize whitespace for cleaner pgAdmin execution
        content = re.sub(r"\s+", " ", content).strip()

        # Ensure terminator
        if content and not content.endswith(';'):
            content += ';'

        return content
    
    def parse_table_response(self, response):
        """Extract table names from AI response"""
        try:
            response = response.strip()
            if response.startswith('```json'):
                response = response[7:-3].strip()
            elif response.startswith('```'):
                response = response[3:-3].strip()
            
            start = response.find('[')
            end = response.rfind(']') + 1
            if start != -1 and end > start:
                json_str = response[start:end]
                tables = json.loads(json_str)
                return tables if isinstance(tables, list) else []
            
            tables = json.loads(response)
            return tables if isinstance(tables, list) else []
            
        except Exception as e:
            print(f"JSON parsing failed: {e}")
            fallback_tables = []
            known_tables = ["Customer", "Risk_Profile", "Transaction_db_new", 
                          "Daily_Transaction_Insurance", "Tasks", "EmployeeProfile"]
            
            for table in known_tables:
                if table in response:
                    fallback_tables.append(table)
            
            return fallback_tables
    
    def generate_query(self, question: str, selected_tables: list = None, filtered_schema: str = None, geometry: Optional[dict] = None):
        """Generate SQL query with conversation context. If geometry is provided, PostGIS SQL is generated."""
        import json as _json
        context = self.memory.get_context_summary()
        token_usage = {"table_selection": {}, "sql_generation": {}}

        # Inject geometry context into the question so LLM generates PostGIS SQL
        if geometry:
            import json as _json_mod
            geometry_json = _json_mod.dumps(geometry)   # clean, valid JSON with double quotes
            geom_type = geometry.get('type', 'Geometry')

            # AUTO-DISCOVER geometry columns from DB schema
            geo_schema_info = self.get_geometry_columns()
            print(f"[GEO SCHEMA] Discovered: {geo_schema_info}")

            # KEY IDEA: Tell LLM to write __GEOJSON__ as placeholder.
            # Python will replace it after with the real JSON string.
            # This prevents LLM from corrupting the JSON with wrong escaping.

            if geom_type == 'Point':
                geo_instruction = (
                    f"\n\n[SPATIAL CONTEXT - CRITICAL] The user provided a POINT geometry."
                    f"\n[DB SCHEMA] {geo_schema_info}"
                    f"\nINSTRUCTIONS:"
                    f"1. Use PostGIS ST_DWithin for radius queries (meters)."
                    f"   - 10km = 10000, 1km = 1000, 100m = 100."
                    f"2. IDENTIFY the correct table & geometry column from schema above."
                    f"3. STRICTLY use the placeholder '__GEOJSON__' inside ST_GeomFromGeoJSON()."
                    f"   - DO NOT write coordinates manually."
                    f"   - DO NOT escape quotes."
                    f"   - JUST write '__GEOJSON__'. Python will replace it."
                    f"4. ONLY generate a SELECT query."
                    f"\nCORRECT PATTERN:"
                    f"SELECT * FROM <table_name> WHERE ST_DWithin(<geom_col>, ST_SetSRID(ST_GeomFromGeoJSON('__GEOJSON__'), 4326), <radius>);"
                )
            else:  # Polygon, MultiPolygon
                geo_instruction = (
                    f"\n\n[SPATIAL CONTEXT - CRITICAL] The user provided a {geom_type} geometry."
                    f"\n[DB SCHEMA] {geo_schema_info}"
                    f"\nINSTRUCTIONS:"
                    f"1. ALWAYS use ST_Intersects for polygon queries (finds overlapping geometries)."
                    f"2. IDENTIFY the correct table & geometry column from schema above."
                    f"3. STRICTLY use the placeholder '__GEOJSON__' inside ST_GeomFromGeoJSON()."
                    f"   - DO NOT write coordinates manually."
                    f"   - DO NOT escape quotes."
                    f"   - JUST write '__GEOJSON__'. Python will replace it."
                    f"4. MUST use ST_SetSRID with EPSG:4326 (standard lat/lon)."
                    f"5. ONLY generate a SELECT query."
                    f"\nCORRECT PATTERN:"
                    f"SELECT * FROM <table_name> WHERE ST_Intersects(<geom_col>, ST_SetSRID(ST_GeomFromGeoJSON('__GEOJSON__'), 4326));"
                )

            question = question + geo_instruction

        # Get relevant tables only if not provided


        if selected_tables is None or filtered_schema is None:
            table_details = self.get_table_details()
            table_response_obj = (self.table_prompt | self.llm).invoke({
                "question": question,
                "table_details": table_details,
                "conversation_context": context
            })
            
            # Extract token usage for table selection
            if hasattr(table_response_obj, 'response_metadata'):
                usage = table_response_obj.response_metadata.get('token_usage', {})
                token_usage["table_selection"] = {
                    "prompt_tokens": usage.get('prompt_tokens', 0),
                    "completion_tokens": usage.get('completion_tokens', 0),
                    "total_tokens": usage.get('total_tokens', 0)
                }
            
            selected_tables = self.parse_table_response(table_response_obj.content)
            filtered_schema = self.get_filtered_schema(selected_tables)
        
        # Generate SQL with conversation history
        chat_history = self.memory.get_langchain_messages()
        query_response = (self.query_prompt | self.llm).invoke({
            "schema": filtered_schema,
            "selected_tables_list": ", ".join(self.selected_tables),
            "question": question,
            "conversation_context": context,
            "chat_history": chat_history[-4:] if chat_history else []
        })
        
        # Extract token usage for SQL generation
        if hasattr(query_response, 'response_metadata'):
            usage = query_response.response_metadata.get('token_usage', {})
            print(f"SQL generation token usage: {usage}")
            token_usage["sql_generation"] = {
                "prompt_tokens": usage.get('prompt_tokens', 0),
                "completion_tokens": usage.get('completion_tokens', 0),
                "total_tokens": usage.get('total_tokens', 0)
            }
        
        final_sql = self._extract_executable_sql(query_response.content)

        # Replace __GEOJSON__ placeholder with the real GeoJSON string
        # This guarantees valid JSON with correct double quotes — no LLM escaping bugs!
        if geometry and '__GEOJSON__' in final_sql:
            import json as _json_replace
            real_json = _json_replace.dumps(geometry)  # always valid JSON, double quotes
            
            # Use PostgreSQL Dollar Quoting ($$) to avoid escaping double quotes
            # This makes the SQL cleaner and prevents Swagger/JSON from adding backslashes (\")
            # Example: ST_GeomFromGeoJSON($${"type": "Point"}$$)
            final_sql = final_sql.replace("'__GEOJSON__'", f"$${real_json}$$")
            final_sql = final_sql.replace('"__GEOJSON__"', f"$${real_json}$$")
            final_sql = final_sql.replace('__GEOJSON__', f"$${real_json}$$")  # Fallback
            
            print(f"[GEO] Replaced __GEOJSON__ placeholder with Dollar Quoted JSON")

        return self.validate_and_fix_sql(final_sql, filtered_schema), selected_tables, filtered_schema, token_usage
    
    def _build_spatial_sql(self, raw_sql: str, geometry: dict) -> str:
        """Post-process spatial SQL: replace __GEOJSON__ placeholder, clean and format."""
        import re as _re
        import json as _json

        sql = raw_sql

        # Replace __GEOJSON__ placeholder with Dollar-Quoted real GeoJSON
        if geometry and '__GEOJSON__' in sql:
            real_json = _json.dumps(geometry)  # always valid JSON, double quotes
            sql = sql.replace("'__GEOJSON__'", f"$${real_json}$$")
            sql = sql.replace('"__GEOJSON__"', f"$${real_json}$$")
            sql = sql.replace('__GEOJSON__', f"$${real_json}$$")  # fallback
            print("[GEO] Replaced __GEOJSON__ placeholder with Dollar Quoted JSON")

        # Restore any erroneously escaped double quotes
        sql = sql.replace('\\"', '"')

        # Single-line format
        sql = sql.strip()
        sql = _re.sub(r'\s+', ' ', sql)
        if not sql.endswith(';'):
            sql = sql + ';'
        return sql

    def process_query(self, question: str, geometry: dict = None):
        """Main function: process query with conversation memory.
        
        Args:
            question: Natural language question from the user.
            geometry: Optional GeoJSON geometry dict (Point, Polygon, etc.).
                      If provided, the pipeline automatically routes to SQL_SPATIAL.
        """
        try:
            # Add user question to memory
            self.memory.add_message("user", question)

            # If geometry is explicitly provided, skip LLM intent check and go spatial directly
            if geometry:
                intent = QueryIntent.SQL_SPATIAL
                intent_tokens = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
                print("[SPATIAL] Geometry provided — forcing SQL_SPATIAL intent (skipping LLM intent call)")
            else:
                # Classify intent via LLM
                intent, intent_tokens = self.classify_intent(question)
                print(f"Detected intent: {intent.value}")

            response_data = None
            total_tokens_used = intent_tokens.get('total_tokens', 0)

            # ── SPATIAL SQL BRANCH ────────────────────────────────────────────────────
            if intent == QueryIntent.SQL_SPATIAL:
                # generate_query already handles geo_instruction injection + __GEOJSON__ replacement
                sql_query, selected_tables, filtered_schema, gen_tokens = self.generate_query(
                    question=question,
                    geometry=geometry
                )

                table_tokens = gen_tokens.get('table_selection', {}).get('total_tokens', 0)
                sql_tokens = gen_tokens.get('sql_generation', {}).get('total_tokens', 0)
                total_tokens_used += table_tokens + sql_tokens

                # ── SAFETY CHECK: block any non-SELECT spatial query ──────────────────
                cleaned_upper = sql_query.strip().upper()
                dangerous_ops = ["UPDATE ", "DELETE ", "INSERT ", "DROP ", "TRUNCATE ", "ALTER ", "CREATE "]
                if any(cleaned_upper.startswith(d) for d in dangerous_ops):
                    raise Exception(
                        "Only SELECT queries are allowed for spatial queries. "
                        "The AI attempted to generate a write query which has been blocked."
                    )

                # ── Build clean display version (single quotes for JSON inside SQL) ──
                import re as _re
                def _replace_json_quotes(match):
                    return match.group(0).replace('"', "'")
                sql_clean = _re.sub(
                    r'ST_GeomFromGeoJSON\((.*?)\)',
                    _replace_json_quotes,
                    sql_query,
                    flags=_re.IGNORECASE
                )
                # Format both to single line
                def _single_line(q):
                    q = q.strip()
                    q = _re.sub(r'\s+', ' ', q)
                    if not q.endswith(';'): q += ';'
                    return q

                sql_strict_final = _single_line(sql_query)
                sql_clean_final  = _single_line(sql_clean)

                response_data = {
                    "status": "success",
                    "intent": "sql_spatial",
                    "question": question,
                    "geometry_provided": geometry is not None,
                    "geometry_type": geometry.get("type") if geometry else None,
                    "sql_query": sql_strict_final,          # executable (pgAdmin)
                    "sql_query_clean": sql_clean_final,     # display (Swagger)
                    "sql_query_pgadmin": sql_strict_final,  # alias kept for backward compat
                    "filtered_tables": selected_tables,
                    "schema_token_size": len(filtered_schema.split()),
                    "note": "Use 'sql_query' / 'sql_query_pgadmin' for execution. 'sql_query_clean' is for easy reading.",
                    "conversation_token_estimate": self.memory.get_token_estimate(),
                    "llm_token_usage": {
                        "intent_classification": intent_tokens,
                        "table_selection": gen_tokens.get('table_selection', {}),
                        "sql_generation": gen_tokens.get('sql_generation', {}),
                        "total_tokens_used": total_tokens_used
                    }
                }

                self.memory.add_message("assistant", "Generated spatial SQL query", {
                    "intent": "sql_spatial",
                    "tables_used": selected_tables
                })

            # ── STANDARD SQL BRANCH ───────────────────────────────────────────────────
            elif intent == QueryIntent.SQL_QUERY:
                sql_query, selected_tables, filtered_schema, gen_tokens = self.generate_query(question)

                table_tokens = gen_tokens.get('table_selection', {}).get('total_tokens', 0)
                sql_tokens = gen_tokens.get('sql_generation', {}).get('total_tokens', 0)
                total_tokens_used += table_tokens + sql_tokens

                response_data = {
                    "status": "success",
                    "intent": "sql_query",
                    "sql_query": sql_query,
                    "filtered_tables": selected_tables,
                    "filtered_schema": filtered_schema,
                    "schema_token_size": len(filtered_schema.split()),
                    "conversation_token_estimate": self.memory.get_token_estimate(),
                    "llm_token_usage": {
                        "intent_classification": intent_tokens,
                        "table_selection": gen_tokens.get('table_selection', {}),
                        "sql_generation": gen_tokens.get('sql_generation', {}),
                        "total_tokens_used": total_tokens_used
                    }
                }

                self.memory.add_message("assistant", "Generated SQL query", {
                    "intent": "sql_query",
                    "tables_used": selected_tables
                })

            # ── CASUAL CHAT ───────────────────────────────────────────────────────────
            elif intent == QueryIntent.CASUAL_CHAT:
                result = self.handle_casual_chat(question)
                response_data = {
                    "status": "success",
                    **result,
                    "conversation_token_estimate": self.memory.get_token_estimate(),
                    "llm_token_usage": {
                        "intent_classification": intent_tokens,
                        "total_tokens_used": total_tokens_used
                    }
                }
                self.memory.add_message("assistant", result["response"], {"intent": "casual_chat"})

            # ── GENERAL KNOWLEDGE ─────────────────────────────────────────────────────
            elif intent == QueryIntent.GENERAL_KNOWLEDGE:
                result = self.handle_general_knowledge(question)
                response_data = {
                    "status": "success",
                    **result,
                    "conversation_token_estimate": self.memory.get_token_estimate(),
                    "llm_token_usage": {
                        "intent_classification": intent_tokens,
                        "total_tokens_used": total_tokens_used
                    }
                }
                self.memory.add_message("assistant", result["response"], {"intent": "general_knowledge"})

            # ── SARCASTIC ─────────────────────────────────────────────────────────────
            elif intent == QueryIntent.SARCASTIC_RESPONSE:
                result = self.handle_sarcastic_response(question)
                response_data = {
                    "status": "success",
                    **result,
                    "conversation_token_estimate": self.memory.get_token_estimate(),
                    "llm_token_usage": {
                        "intent_classification": intent_tokens,
                        "total_tokens_used": total_tokens_used
                    }
                }
                self.memory.add_message("assistant", result["response"], {"intent": "sarcastic_response"})

            # ── AMBIGUOUS ─────────────────────────────────────────────────────────────
            else:
                try:
                    sql_query, selected_tables, filtered_schema, gen_tokens = self.generate_query(question)
                    table_tokens = gen_tokens.get('table_selection', {}).get('total_tokens', 0)
                    sql_tokens = gen_tokens.get('sql_generation', {}).get('total_tokens', 0)
                    total_tokens_used += table_tokens + sql_tokens

                    response_data = {
                        "status": "success",
                        "intent": "sql_query",
                        "sql_query": sql_query,
                        "filtered_schema": filtered_schema,
                        "note": "Intent was ambiguous, attempted SQL generation",
                        "conversation_token_estimate": self.memory.get_token_estimate(),
                        "llm_token_usage": {
                            "intent_classification": intent_tokens,
                            "table_selection": gen_tokens.get('table_selection', {}),
                            "sql_generation": gen_tokens.get('sql_generation', {}),
                            "total_tokens_used": total_tokens_used
                        }
                    }
                    self.memory.add_message("assistant", "Generated SQL from ambiguous query", {
                        "intent": "ambiguous_sql"
                    })
                except Exception as e:
                    response_msg = "Your question is unclear. Please rephrase your question."
                    response_data = {
                        "status": "error",
                        "intent": "ambiguous",
                        "response": response_msg,
                        "conversation_token_estimate": self.memory.get_token_estimate(),
                        "llm_token_usage": {
                            "intent_classification": intent_tokens,
                            "total_tokens_used": total_tokens_used
                        }
                    }
                    self.memory.add_message("assistant", response_msg, {"intent": "ambiguous_error"})

            return response_data

        except Exception as e:
            raise Exception(f"Query processing failed: {str(e)}")
    
    def get_conversation_history(self) -> Dict:
        """Export conversation history"""
        return self.memory.to_dict()
    
    def load_conversation_history(self, history_data: Dict):
        """Import conversation history"""
        self.memory.from_dict(history_data)
    
    def clear_conversation(self):
        """Clear conversation history"""
        self.memory.clear()
        print(f"Conversation history cleared for session: {self.memory.session_id}")
    
    def fix_sql_query(self, failed_query: str, error_message: str, schema: str) -> tuple:
        """Fix SQL query based on error message"""
        token_usage = {}
        try:
            fixed_response = (self.sql_fix_prompt | self.llm).invoke({
                "schema": schema,
                "failed_query": failed_query,
                "error_message": error_message
            })
            
            # Extract token usage
            if hasattr(fixed_response, 'response_metadata'):
                usage = fixed_response.response_metadata.get('token_usage', {})
                token_usage = {
                    "prompt_tokens": usage.get('prompt_tokens', 0),
                    "completion_tokens": usage.get('completion_tokens', 0),
                    "total_tokens": usage.get('total_tokens', 0)
                }
            
            cleaned = fixed_response.content.replace("```sql", "").replace("```", "").strip()
            return self.validate_and_fix_sql(cleaned, schema), token_usage
        except Exception as e:
            print(f"SQL fix failed: {e}")
            return failed_query, token_usage
