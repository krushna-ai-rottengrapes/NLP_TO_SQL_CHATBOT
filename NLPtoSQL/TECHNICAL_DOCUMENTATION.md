# NLP to SQL - Technical Documentation

## Overview
This document explains the technical implementation of the NLP to SQL conversion system, focusing on `query_engine.py` and `connection.py`.

---

## File 1: `backend/Langchain/query_engine.py`

### Purpose
Converts natural language questions into SQL queries using LangChain and Groq LLM, with conversation memory management.

---

## Class 1: `QueryIntent` (Enum)

### Purpose
Defines the types of user questions the system can handle.

### Values
- `SQL_QUERY` - Database-related questions
- `CASUAL_CHAT` - Greetings, small talk
- `GENERAL_KNOWLEDGE` - Non-database questions
- `SARCASTIC_RESPONSE` - Troll/irrelevant questions
- `AMBIGUOUS` - Unclear questions

---

## Class 2: `ConversationMemory`

### Purpose
Manages conversation history with smart token optimization to prevent exceeding LLM token limits.

### Constructor: `__init__(max_exchanges=5, max_tokens_per_msg=500)`

**Parameters:**
- `max_exchanges` (int): Maximum number of conversation exchanges to store (default: 5)
  - Each exchange = 1 user message + 1 AI response
  - Total messages stored = max_exchanges × 2 = 10 messages
- `max_tokens_per_msg` (int): Maximum tokens per message (default: 500)

**Attributes:**
- `messages` (deque): Circular buffer storing last N exchanges
- `session_id` (str): Unique session identifier
- `created_at` (datetime): Session creation timestamp

**How it works:**
```python
self.messages = deque(maxlen=max_exchanges * 2)
```
- Uses `deque` with `maxlen` - automatically removes oldest messages when limit reached
- Stores 10 messages (5 user + 5 AI) by default

---

### Method: `add_message(role, content, metadata=None)`

**Purpose:** Add a message to conversation history with automatic truncation.

**Parameters:**
- `role` (str): "user" or "assistant"
- `content` (str): Message content
- `metadata` (dict): Optional metadata (intent, tables used, etc.)

**Token Truncation Logic - DETAILED EXPLANATION:**

```python
if len(content) > self.max_tokens_per_msg * 4:  # Approx 4 chars per token
    content = content[:self.max_tokens_per_msg * 4] + "... [truncated]"
```

**How This Works:**

1. **Token Estimation:**
   - LLMs use "tokens" (word pieces) for processing
   - Rough estimate: **4 characters ≈ 1 token**
   - Example: "Hello world" = 11 chars ≈ 2.75 tokens ≈ 3 tokens

2. **Calculation:**
   - `max_tokens_per_msg = 500` (default)
   - Maximum characters allowed = `500 × 4 = 2000 characters`

3. **Condition Check:**
   - `len(content)` = actual character count in message
   - If message has **more than 2000 characters**, it gets truncated

4. **Truncation Process:**
   - `content[:self.max_tokens_per_msg * 4]` = Keep first 2000 characters
   - `+ "... [truncated]"` = Add indicator that content was cut

**Example:**

```python
# Scenario 1: Short message (no truncation)
content = "Show me all customers"  # 20 chars
# 20 < 2000, so NO truncation

# Scenario 2: Long message (truncation happens)
content = "A" * 3000  # 3000 chars
# 3000 > 2000, so:
# content = "AAA...AAA (first 2000 chars)... [truncated]"
```

**Why This Matters:**
- Prevents memory overflow
- Keeps conversation context manageable
- Avoids exceeding LLM token limits (most models have 4K-8K token limits)
- Saves API costs (fewer tokens = cheaper)

---

### Method: `get_langchain_messages()`

**Purpose:** Convert stored messages to LangChain format for LLM processing.

**Returns:** List of `HumanMessage` and `AIMessage` objects

**How it works:**
```python
for msg in self.messages:
    if msg["role"] == "user":
        lc_messages.append(HumanMessage(content=msg["content"]))
    elif msg["role"] == "assistant":
        lc_messages.append(AIMessage(content=msg["content"]))
```

Transforms internal format → LangChain format for LLM consumption.

---

### Method: `get_context_summary()`

**Purpose:** Generate compact summary of recent conversation.

**Returns:** String with last 3 exchanges (6 messages)

**How it works:**
```python
for msg in list(self.messages)[-6:]:  # Last 3 exchanges
    role = "User" if msg["role"] == "user" else "Assistant"
    content = msg["content"][:200]  # First 200 chars only
    summary_parts.append(f"{role}: {content}")
```

- Takes last 6 messages
- Truncates each to 200 characters
- Creates readable summary for context injection

---

### Method: `get_token_estimate()`

**Purpose:** Estimate total tokens in conversation history.

**Formula:**
```python
total_chars = sum(len(msg["content"]) for msg in self.messages)
return total_chars // 4  # Integer division
```

**Example:**
- Message 1: 100 chars
- Message 2: 200 chars
- Total: 300 chars ÷ 4 = 75 tokens (estimated)

---

### Method: `to_dict()` and `from_dict(data)`

**Purpose:** Export/import conversation history for persistence.

**Use case:** Save conversation to database, restore later

---

## Class 3: `QueryEngine`

### Purpose
Main engine that orchestrates NLP to SQL conversion with intent detection and memory.

---

### Constructor: `__init__(db, csv_path, session_id=None)`

**Parameters:**
- `db` (SQLDatabase): LangChain database connection
- `csv_path` (str): Path to table catalog CSV
- `session_id` (str): Optional session identifier

**Initialization Steps:**

1. **Setup Memory:**
```python
self.memory = ConversationMemory(max_exchanges=5, max_tokens_per_msg=500)
self.memory.session_id = session_id or f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
```

2. **Setup Groq LLM:**
```python
self.llm = ChatGroq(
    temperature=0,  # Deterministic responses
    model_name="llama-3.3-70b-versatile",
    groq_api_key=os.environ["GROQ_API_KEY"]
)
```

3. **Setup Web Search:**
```python
self.search_tool = DuckDuckGoSearchRun()
```

4. **Create AI Prompts:**
```python
self._setup_chains()
```

---

### Method: `_setup_chains()`

**Purpose:** Create all AI prompt templates with conversation memory support.

**Creates 5 Chains:**

1. **Intent Detection Chain:**
   - Classifies user question type
   - Uses conversation context for better classification
   - Returns: SQL_QUERY, CASUAL_CHAT, GENERAL_KNOWLEDGE, SARCASTIC_RESPONSE, or AMBIGUOUS

2. **SQL Generation Chain:**
   - Generates SQL from natural language
   - Includes database schema
   - Uses conversation context for pronoun resolution
   - Has strict rules for PostgreSQL syntax

3. **Table Selection Chain:**
   - Selects relevant tables for query
   - Returns JSON array of table names

4. **Sarcastic Response Chain:**
   - Generates witty responses for irrelevant questions

5. **SQL Error Correction Chain:**
   - Fixes failed SQL queries based on error messages

---

### Method: `classify_intent(question)`

**Purpose:** Determine what type of question the user is asking.

**Process:**

1. Get conversation context:
```python
context = self.memory.get_context_summary()
chat_history = self.memory.get_langchain_messages()
```

2. Invoke intent chain with context:
```python
intent_response = self.intent_chain.invoke({
    "question": question,
    "conversation_context": context,
    "chat_history": chat_history[-4:]  # Last 2 exchanges
})
```

3. Parse response and return intent enum

**Why Context Matters:**
- User: "Show me customers in Mumbai"
- AI: "Here are 50 customers"
- User: "What about Delhi?" ← Context helps understand "Delhi" refers to customers

---

### Method: `generate_query(question, selected_tables=None, filtered_schema=None)`

**Purpose:** Generate SQL query from natural language.

**Process:**

1. **Get Conversation Context:**
```python
context = self.memory.get_context_summary()
```

2. **Select Relevant Tables** (if not provided):
```python
table_response = self.table_chain.invoke({
    "question": question,
    "table_details": table_details,
    "conversation_context": context
})
selected_tables = self.parse_table_response(table_response)
```

3. **Filter Schema** (only include relevant tables):
```python
filtered_schema = self.get_filtered_schema(selected_tables)
```

**Why Filter Schema?**
- Full schema = 50 tables × 20 columns = 1000 lines
- Filtered schema = 2 tables × 20 columns = 40 lines
- Saves tokens, improves accuracy, reduces cost

4. **Generate SQL with Context:**
```python
chat_history = self.memory.get_langchain_messages()
query_response = (self.query_prompt | self.llm).invoke({
    "schema": filtered_schema,
    "question": question,
    "conversation_context": context,
    "chat_history": chat_history[-4:]
})
```

5. **Clean and Validate SQL:**
```python
sql_content = query_response.content.replace("```sql", "").replace("```", "").strip()
final_sql = self.validate_and_fix_sql(sql_content, filtered_schema)
```

---

### Method: `validate_and_fix_sql(sql_query, schema="")`

**Purpose:** Fix common SQL syntax errors using regex.

**Fixes Applied:**

1. **Double Qualification Fix:**
```python
# Pattern 1: crm_customer.c.id → c.id
sql_query = re.sub(r'\b(\w+)\.([a-z])\.(\w+)\b', r'\2.\3', sql_query)

# Pattern 2: alias.table.column → alias.column
sql_query = re.sub(r'\b([a-z])\.(\w+)\.(\w+)\b', r'\1.\3', sql_query)

# Pattern 3: table.table.column → table.column
sql_query = re.sub(r'\b(\w+)\.(\1)\.(\w+)\b', r'\1.\3', sql_query)
```

**Example:**
```sql
-- Before: WRONG
SELECT c.crm_customer.name FROM crm_customer c

-- After: CORRECT
SELECT c.name FROM crm_customer c
```

---

### Method: `process_query(question)`

**Purpose:** Main entry point - processes user question end-to-end.

**Flow:**

1. **Add to Memory:**
```python
self.memory.add_message("user", question)
```

2. **Classify Intent:**
```python
intent = self.classify_intent(question)
```

3. **Route Based on Intent:**

   **If SQL_QUERY:**
   - Generate SQL
   - Return SQL + metadata
   - Add to memory

   **If CASUAL_CHAT:**
   - Generate friendly response
   - Return response
   - Add to memory

   **If GENERAL_KNOWLEDGE:**
   - Perform web search
   - Summarize results
   - Return response
   - Add to memory

   **If SARCASTIC_RESPONSE:**
   - Generate witty response
   - Return response
   - Add to memory

   **If AMBIGUOUS:**
   - Try SQL generation
   - If fails, ask for clarification

4. **Return Response with Token Estimate:**
```python
response_data = {
    "status": "success",
    "intent": "sql_query",
    "sql_query": sql_query,
    "conversation_token_estimate": self.memory.get_token_estimate()
}
```

---

### Method: `fix_sql_query(failed_query, error_message, schema)`

**Purpose:** Use LLM to fix failed SQL queries.

**Process:**
1. Send failed query + error message + schema to LLM
2. LLM analyzes error and generates corrected query
3. Validate and return fixed query

**Example:**
```python
# Failed Query:
SELECT * FROM customer_table  # Table doesn't exist

# Error:
relation "customer_table" does not exist

# LLM Fix:
SELECT * FROM crm_customer  # Correct table name
```

---

## File 2: `backend/database/connection.py`

### Purpose
FastAPI router that handles database connections, query execution, and conversation management.

---

## Class: `DatabaseConfig` (Pydantic Model)

**Purpose:** Validate database connection parameters.

**Fields:**
- `db_type`: "postgres" or "mssql"
- `db_user`: Database username
- `db_password`: Database password
- `db_host`: Database host/IP
- `db_name`: Database name
- `db_port`: Database port

---

## Class: `DatabaseConnection`

### Static Method: `connect(config)`

**Purpose:** Create database connection URI and connect.

**Process:**

1. **Build Connection URI:**
```python
# PostgreSQL
connection_uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"

# MSSQL
encoded_password = quote(password, safe='')
connection_uri = f"mssql+pymssql://{user}:{encoded_password}@{host}:{port}/{db_name}"
```

2. **Create SQLDatabase Object:**
```python
db = SQLDatabase.from_uri(connection_uri, sample_rows_in_table_info=1)
```

---

## API Endpoints

### POST `/database/connect`

**Purpose:** Connect to database and initialize query engine with session.

**Parameters:**
- Form data: db_type, db_user, db_password, db_host, db_name, db_port
- Optional: csv_file (table catalog)
- Optional: session_id

**Process:**

1. **Handle CSV Upload:**
```python
if csv_file:
    content = await csv_file.read()
    csv_path = f"static/{csv_file.filename}"
    with open(csv_path, "wb") as f:
        f.write(content)
```

2. **Connect to Database:**
```python
db = DatabaseConnection.connect(config)
```

3. **Initialize Query Engine with Session:**
```python
query_engine = QueryEngine(current_db, current_csv_path, session_id=session_id)
```

4. **Return Connection Info:**
```python
return {
    "status": "success",
    "session_id": query_engine.memory.session_id,
    "database_info": {...},
    "memory_config": {
        "max_exchanges": 5,
        "max_tokens_per_message": 500,
        "current_messages": 0
    }
}
```

---

### POST `/database/query`

**Purpose:** Process NLP query and return SQL (without execution).

**Request:**
```json
{
  "question": "Show me all customers in Mumbai"
}
```

**Response:**
```json
{
  "status": "success",
  "intent": "sql_query",
  "question": "Show me all customers in Mumbai",
  "sql_query": "SELECT * FROM crm_customer WHERE city = 'Mumbai'",
  "filtered_tables": ["crm_customer"],
  "schema_token_size": 150,
  "conversation_token_estimate": 75
}
```

**Process:**
```python
result = query_engine.process_query(request.question)
```

---

### POST `/database/query-and-execute`

**Purpose:** Generate SQL and execute it, returning results.

**Process:**

1. **Generate SQL:**
```python
result = query_engine.process_query(request.question)
```

2. **Execute SQL:**
```python
exec_result = await execute_sql_query(sql_request)
```

3. **Return Combined Response:**
```json
{
  "status": "success",
  "intent": "sql_query",
  "sql_query": "SELECT ...",
  "data": [{...}, {...}],
  "columns": ["id", "name", "city"],
  "note": "SQL generated and executed successfully"
}
```

---

### POST `/database/execute-sql`

**Purpose:** Execute SQL with auto-retry and LLM correction (max 5 attempts).

**How Auto-Retry Works:**

```python
max_retries = 5
current_query = request.sql_query

for attempt in range(max_retries):
    try:
        result = execute_sql_direct(current_query)
        return result  # Success!
    except Exception as e:
        error_msg = str(e)
        
        # Last attempt - give up
        if attempt == max_retries - 1:
            raise HTTPException(...)
        
        # Try to fix with LLM
        current_query = query_engine.fix_sql_query(
            current_query, 
            error_msg, 
            schema
        )
```

**Example Flow:**

```
Attempt 1: SELECT * FROM customer_table
Error: Table doesn't exist

Attempt 2: SELECT * FROM crm_customer WHERE city = Mumbai
Error: Column "city" doesn't exist (unquoted string)

Attempt 3: SELECT * FROM crm_customer WHERE city = 'Mumbai'
Success! ✓
```

---

### GET `/database/conversation/history`

**Purpose:** Get current conversation history.

**Response:**
```json
{
  "status": "success",
  "session_id": "session_20240115_143022",
  "created_at": "2024-01-15T14:30:22",
  "message_count": 6,
  "token_estimate": 450,
  "messages": [
    {
      "role": "user",
      "content": "Show me customers",
      "timestamp": "2024-01-15T14:30:25",
      "metadata": {}
    },
    {
      "role": "assistant",
      "content": "Generated SQL query",
      "timestamp": "2024-01-15T14:30:27",
      "metadata": {"intent": "sql_query", "tables_used": ["crm_customer"]}
    }
  ]
}
```

---

### POST `/database/conversation/clear`

**Purpose:** Clear conversation history and start fresh session.

**Response:**
```json
{
  "status": "success",
  "message": "Conversation history cleared",
  "previous_session": "session_20240115_143022",
  "new_session": "session_20240115_150000"
}
```

---

### GET `/database/conversation/stats`

**Purpose:** Get detailed conversation statistics.

**Response:**
```json
{
  "status": "success",
  "session_id": "session_20240115_143022",
  "total_messages": 10,
  "user_messages": 5,
  "ai_messages": 5,
  "token_estimate": 850,
  "max_exchanges_limit": 5,
  "intent_breakdown": {
    "sql_query": 3,
    "casual_chat": 1,
    "general_knowledge": 1
  },
  "memory_usage": {
    "current_exchanges": 5,
    "max_exchanges": 5,
    "utilization_percent": 100.0
  }
}
```

---

## Function: `execute_sql_direct(sql_query)`

**Purpose:** Execute SQL directly on database (PostgreSQL or MSSQL).

**Process:**

1. **Clean Query:**
```python
cleaned_query = sql_query.strip().replace("```sql", "").replace("```", "")
```

2. **Handle Multiple Statements:**
```python
statements = [s.strip() for s in cleaned_query.split(';') if s.strip()]
# Combine CTE + SELECT if needed
```

3. **Fix Column Casing (PostgreSQL):**
```python
if current_db_config.db_type.lower() == "postgres":
    cleaned_query = fix_column_casing(cleaned_query)
```

4. **Execute Based on DB Type:**

**PostgreSQL:**
```python
conn = psycopg2.connect(host, port, database, user, password)
cursor = conn.cursor()
cursor.execute(cleaned_query)
columns = [desc[0] for desc in cursor.description]
results = cursor.fetchall()
```

**MSSQL:**
```python
conn = pymssql.connect(server, port, database, user, password)
cursor = conn.cursor()
cursor.execute(cleaned_query)
columns = [desc[0] for desc in cursor.description]
results = cursor.fetchall()
```

5. **Format Results:**
```python
data = []
for row in results:
    row_dict = {}
    for col, val in zip(columns, row):
        row_dict[col] = serialize_datetime(val)
    data.append(row_dict)
```

6. **Categorize Columns:**
```python
data_types = categorize_columns(data, columns)
# Returns: {"id": "scalar", "transactions": "array"}
```

---

## Key Concepts Summary

### 1. Token Management
- **4 characters ≈ 1 token** (estimation rule)
- Messages truncated at 2000 chars (500 tokens)
- Conversation limited to 5 exchanges (10 messages)
- Prevents token overflow and reduces costs

### 2. Conversation Memory
- Circular buffer (deque) with automatic eviction
- Stores last 5 user-AI exchanges
- Provides context for pronoun resolution
- Enables multi-turn conversations

### 3. Intent Classification
- Routes questions to appropriate handlers
- Uses conversation context for better accuracy
- 5 intent types: SQL, Chat, Knowledge, Sarcastic, Ambiguous

### 4. Schema Filtering
- Reduces token usage by 90%+
- Improves SQL generation accuracy
- Only includes relevant tables in prompt

### 5. Auto-Retry with LLM Correction
- Attempts query execution up to 5 times
- Uses LLM to fix errors automatically
- Learns from error messages

### 6. Session Management
- Each connection gets unique session ID
- Conversation history tied to session
- Can export/import history for persistence

---

## Performance Optimizations

1. **Token Truncation:** Prevents memory overflow
2. **Schema Filtering:** Reduces prompt size by 90%
3. **Circular Buffer:** O(1) message addition/removal
4. **Context Summary:** Only last 3 exchanges (not full history)
5. **Lazy Loading:** Only load schema for relevant tables

---

## Error Handling

1. **SQL Syntax Errors:** Auto-fix with regex + LLM
2. **Table Not Found:** LLM suggests correct table name
3. **Column Not Found:** LLM checks schema and fixes
4. **Ambiguous Queries:** Ask user for clarification
5. **Token Overflow:** Automatic truncation

---

## End of Documentation
