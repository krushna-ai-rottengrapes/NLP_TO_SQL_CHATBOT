from fastapi import APIRouter, HTTPException, Depends, Body
from langchain_community.utilities.sql_database import SQLDatabase
from urllib.parse import quote
from pydantic import BaseModel
from sqlalchemy.orm import Session
from Langchain import QueryEngine
from auth import get_current_user
from users.models import User
from database.models import Database as DBModel
from db_config import get_db

import psycopg2
import pymysql
import pymssql
import json
import re
import warnings
from datetime import datetime
from typing import Optional, Dict
from utils.encryption import decrypt_password

# Suppress SQLAlchemy warnings for unknown column types
warnings.filterwarnings('ignore', category=Warning, module='sqlalchemy')

router = APIRouter(prefix="/database", tags=["database"])

# In-memory store for user database connections (acts as Redis for now)
user_db_store: Dict[int, Dict] = {}

class ConnectRequest(BaseModel):
    database_id: int

def create_connection_uri(db_record: DBModel, plain_password: str) -> str:
    """Create database connection URI from database record"""
    encoded_password = quote(plain_password, safe='')
    
    if db_record.provider.value == "postgres":
        return f"postgresql+psycopg2://{db_record.user}:{encoded_password}@{db_record.host}:{db_record.port}/{db_record.db_name}"
    elif db_record.provider.value == "mysql":
        return f"mysql+pymysql://{db_record.user}:{encoded_password}@{db_record.host}:{db_record.port}/{db_record.db_name}"
    elif db_record.provider.value == "mssql":
        return f"mssql+pymssql://{db_record.user}:{encoded_password}@{db_record.host}:{db_record.port}/{db_record.db_name}"
    else:
        raise ValueError(f"Unsupported database provider: {db_record.provider}")



@router.post("/connect")
async def connect_database(
    request: ConnectRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Connect to database using database_id from user's databases"""
    try:
        # Get database record
        db_record = db.query(DBModel).filter(DBModel.id == request.database_id).first()
        if not db_record:
            raise HTTPException(status_code=404, detail="Database not found")
        
        # Check access
        if current_user.role.value != "internal_superuser" and db_record.client_id != current_user.client_id:
            raise HTTPException(status_code=403, detail="Access denied")
        
        # Decrypt password
        plain_password = decrypt_password(db_record.password)
        
        # Create connection
        connection_uri = create_connection_uri(db_record, plain_password)
        sql_db = SQLDatabase.from_uri(
            connection_uri,
            sample_rows_in_table_info=1,
            engine_args={"pool_pre_ping": True, "pool_recycle": 300}
        )
        
        # Initialize QueryEngine with dynamic metadata
        query_engine = QueryEngine(
            db=sql_db,
            db_description=db_record.db_description or "database",
            table_descriptions=db_record.description or {},
            selected_tables=db_record.selected_tables or [],
            session_id=f"user_{current_user.id}_db_{request.database_id}",
            stored_schema=db_record.schema  # Pass stored schema to QueryEngine
        )
        
        # Store in user_db_store
        user_db_store[current_user.id] = {
            "db_instance": sql_db,
            "query_engine": query_engine,
            "db_record": db_record,
            "description": db_record.description,
            "db_description": db_record.db_description,
            "plain_password": plain_password,
            "connected_at": datetime.now().isoformat()
        }
        
        return {
            "status": "success",
            "message": f"Connected to {db_record.provider.value} database successfully",
            "database_id": db_record.id,
            "database_name": db_record.db_name,
            "session_id": query_engine.memory.session_id,
            "database_info": {
                "provider": db_record.provider.value,
                "table_count": len(sql_db.get_usable_table_names()),
                "has_description": bool(db_record.description)
            }
        }
        
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=401, detail="Invalid database password")
    except Exception as e:
        import traceback
        print(f"CRITICAL DATABASE CONNECTION ERROR: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

class QueryRequest(BaseModel):
    question: str
    geometry: Optional[Dict] = None  # Optional GeoJSON geometry (Point, Polygon, etc.) for spatial queries

    class Config:
        json_schema_extra = {
            "example": {
                "question": "Find farms within 10km of this point",
                "geometry": {
                    "type": "Point",
                    "coordinates": [76.49, 23.25]
                }
            }
        }

class QueryResponse(BaseModel):
    status: str
    intent: str
    question: str
    sql_query: Optional[str] = None
    response: Optional[str] = None
    filtered_tables: Optional[list] = None
    schema_token_size: Optional[int] = None
    conversation_token_estimate: Optional[int] = None
    llm_token_usage: Optional[Dict] = None
    note: Optional[str] = None
    data: Optional[list] = None
    columns: Optional[list] = None

class GeoQueryRequest(BaseModel):
    question: str
    geometry: Optional[Dict] = None  # GeoJSON geometry (Point, Polygon, etc.)

    class Config:
        json_schema_extra = {
            "example": {
                "question": "  ",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        
                    ]]
                }
            }
        }

class SQLExecuteRequest(BaseModel):
    sql_query: str
    filtered_tables: Optional[list] = None

class ConversationHistoryRequest(BaseModel):
    history_data: Dict


def initialize_db_connection():
    """Initialize database at startup - no longer needed with user-based connections"""
    print("Using user-based database connections. No global initialization needed.")
    pass

@router.post("/query", response_model=QueryResponse)
async def execute_nlp_query(
    request: QueryRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Unified NLP query endpoint.
    - Standard text questions → generates & executes SQL.
    - Questions with spatial words OR geometry provided → routes to spatial SQL pipeline (SELECT only).
    """
    try:
        print(f"Processing query for user {current_user.id}: {request.question}")
        if current_user.id not in user_db_store:
            raise HTTPException(
                status_code=503,
                detail="No database connected. Please connect to a database first using /database/connect"
            )

        user_data = user_db_store[current_user.id]
        query_engine = user_data["query_engine"]

        # Pass geometry (if any) — process_query handles routing internally
        result = query_engine.process_query(request.question, geometry=request.geometry)

        intent = result.get("intent")

        response_data = {
            "status": result.get("status", "success"),
            "intent": intent or "unknown",
            "question": request.question,
            "conversation_token_estimate": result.get("conversation_token_estimate", 0),
            "llm_token_usage": result.get("llm_token_usage", {})
        }

        if intent == "sql_query":
            response_data.update({
                "sql_query": result.get("sql_query"),
                "filtered_tables": result.get("filtered_tables"),
                "schema_token_size": result.get("schema_token_size"),
                "note": result.get("note")
            })

        elif intent == "sql_spatial":
            # Spatial query: return both versions of the SQL
            response_data.update({
                "sql_query": result.get("sql_query"),           # executable (pgAdmin)
                "filtered_tables": result.get("filtered_tables"),
                "schema_token_size": result.get("schema_token_size"),
                "note": result.get("note"),
                # Extra spatial fields (accessible to clients that know about them)
                "sql_query_clean": result.get("sql_query_clean"),
                "sql_query_pgadmin": result.get("sql_query_pgadmin"),
                "geometry_provided": result.get("geometry_provided"),
                "geometry_type": result.get("geometry_type"),
            })

        elif intent in ["casual_chat", "sarcastic_response"]:
            response_data.update({
                "response": result.get("response")
            })

        else:
            response_data.update({
                "response": result.get("response"),
                "sql_query": result.get("sql_query"),
                "filtered_tables": result.get("filtered_tables"),
                "note": result.get("note", "Query intent unclear. Please rephrase.")
            })

        return response_data

    except HTTPException:
        raise
    except Exception as e:
        print(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")


@router.post("/geo-query")
async def execute_geo_nlp_query(
    request: GeoQueryRequest = Body(
        example={
            "question": "  ",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[]]
            }
        }
    ),
    current_user: User = Depends(get_current_user)
):
    """
    [DEPRECATED - use /database/query instead]
    Backward-compatible alias. Internally calls the unified /query pipeline.

    Generate a PostGIS-compatible SQL query from an NLP question + optional GeoJSON geometry.
    The SQL query is returned WITHOUT execution — copy it and run in pgAdmin.

    - Works with Polygon, Point (100km radius), MultiPolygon geometry types.
    - ONLY generates SELECT queries (no UPDATE/DELETE/INSERT).
    """
    try:
        print(f"[geo-query alias] Routing to unified pipeline for user {current_user.id}")
        if current_user.id not in user_db_store:
            raise HTTPException(
                status_code=503,
                detail="No database connected. Please connect first using /database/connect"
            )

        user_data = user_db_store[current_user.id]
        qe = user_data["query_engine"]

        # Route through the unified process_query with geometry
        result = qe.process_query(request.question, geometry=request.geometry)

        # Return in the original geo-query response format for backward compatibility
        return {
            "status": result.get("status", "success"),
            "question": request.question,
            "geometry_provided": request.geometry is not None,
            "geometry_type": request.geometry.get("type") if request.geometry else None,
            "sql_query_clean": result.get("sql_query_clean"),
            "sql_query_pgadmin": result.get("sql_query_pgadmin") or result.get("sql_query"),
            "filtered_tables": result.get("filtered_tables"),
            "note": "[geo-query is deprecated] Use /database/query with a geometry field instead. " + (result.get("note") or ""),
            "llm_token_usage": result.get("llm_token_usage")
        }

    except HTTPException:
        raise
    except Exception as e:
        print(f"Geo-query error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Geo-query failed: {str(e)}")


@router.get("/conversation/history")
async def get_conversation_history():

    """Get current conversation history"""
    try:
        if query_engine is None:
            raise HTTPException(status_code=503, detail="Query engine not initialized")
        
        history = query_engine.get_conversation_history()
        
        return {
            "status": "success",
            "session_id": history["session_id"],
            "created_at": history["created_at"],
            "message_count": history["message_count"],
            "token_estimate": history["token_estimate"],
            "messages": history["messages"],
            "memory_config": {
                "max_exchanges": query_engine.memory.max_exchanges,
                "max_tokens_per_message": query_engine.memory.max_tokens_per_msg
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get history: {str(e)}")

@router.post("/conversation/load")
async def load_conversation_history(request: ConversationHistoryRequest):
    """Load previous conversation history"""
    try:
        if query_engine is None:
            raise HTTPException(status_code=503, detail="Query engine not initialized")
        
        query_engine.load_conversation_history(request.history_data)
        
        return {
            "status": "success",
            "message": "Conversation history loaded successfully",
            "session_id": query_engine.memory.session_id,
            "message_count": len(query_engine.memory.messages),
            "token_estimate": query_engine.memory.get_token_estimate()
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load history: {str(e)}")

@router.post("/conversation/clear")
async def clear_conversation():
    """Clear current conversation history"""
    try:
        if query_engine is None:
            raise HTTPException(status_code=503, detail="Query engine not initialized")
        
        old_session = query_engine.memory.session_id
        query_engine.clear_conversation()
        
        return {
            "status": "success",
            "message": "Conversation history cleared",
            "previous_session": old_session,
            "new_session": query_engine.memory.session_id
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to clear history: {str(e)}")

@router.get("/conversation/stats")
async def get_conversation_stats():
    """Get conversation statistics"""
    try:
        if query_engine is None:
            raise HTTPException(status_code=503, detail="Query engine not initialized")
        
        memory = query_engine.memory
        messages = list(memory.messages)
        
        user_messages = sum(1 for m in messages if m["role"] == "user")
        ai_messages = sum(1 for m in messages if m["role"] == "assistant")
        
        intent_counts = {}
        for msg in messages:
            if msg["role"] == "assistant":
                intent = msg.get("metadata", {}).get("intent", "unknown")
                intent_counts[intent] = intent_counts.get(intent, 0) + 1
        
        return {
            "status": "success",
            "session_id": memory.session_id,
            "created_at": memory.created_at.isoformat(),
            "total_messages": len(messages),
            "user_messages": user_messages,
            "ai_messages": ai_messages,
            "token_estimate": memory.get_token_estimate(),
            "max_exchanges_limit": memory.max_exchanges,
            "intent_breakdown": intent_counts,
            "memory_usage": {
                "current_exchanges": len(messages) // 2,
                "max_exchanges": memory.max_exchanges,
                "utilization_percent": round((len(messages) // 2) / memory.max_exchanges * 100, 1)
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get stats: {str(e)}")

@router.post("/test-intent")
async def test_intent_classification(request: QueryRequest):
    """Test intent classification"""
    try:
        if query_engine is None:
            raise HTTPException(status_code=503, detail="Query engine not initialized")
        
        intent = query_engine.classify_intent(request.question)
        
        intent_descriptions = {
            "sql_query": "Business/database related - Will generate SQL",
            "casual_chat": "Casual conversation - Web search",
            "sarcastic_response": "Irrelevant/troll - Witty response",
            "ambiguous": "Unclear - May need clarification"
        }
        
        return {
            "question": request.question,
            "detected_intent": intent.value,
            "description": intent_descriptions.get(intent.value, "Unknown"),
            "conversation_context_used": query_engine.memory.get_token_estimate() > 0,
            "messages_in_memory": len(query_engine.memory.messages)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Intent classification failed: {str(e)}")

@router.post("/execute-sql")
async def execute_sql_query(
    request: SQLExecuteRequest,
    current_user: User = Depends(get_current_user)
):
    """Execute SQL query with auto-retry and LLM correction (max 5 attempts) with token tracking"""
    # Check if query is a read-only warning message
    if "I can only generate SELECT queries" in request.sql_query or "cannot modify the database" in request.sql_query:
        raise HTTPException(status_code=400, detail="Query rejected: Data modification not allowed. Only SELECT queries are permitted.")
    
    # Get user's database connection
    if current_user.id not in user_db_store:
        raise HTTPException(status_code=503, detail="No database connected")
    
    user_data = user_db_store[current_user.id]
    query_engine = user_data["query_engine"]
    db_instance = user_data["db_instance"]
    db_record = user_data["db_record"]
    plain_password = user_data.get("plain_password")
    
    max_retries = 5
    current_query = request.sql_query
    filtered_tables = request.filtered_tables
    retry_token_usage = []
    
    # Get filtered schema once if tables provided
    schema = None
    if filtered_tables and query_engine:
        schema = query_engine.get_filtered_schema(filtered_tables)
    
    for attempt in range(max_retries):
        try:
            result = execute_sql_direct(current_query, db_record, plain_password)
            
            data_types = result.get("data_types", {})
            if not data_types and result["data"]:
                for col in result["columns"]:
                    is_array = any(isinstance(row.get(col), list) for row in result["data"])
                    data_types[col] = "array" if is_array else "scalar"
            
            # Segregate data into cards and tables
            cards = []
            tables = []
            
            if result["data"] and len(result["data"]) == 1:
                row = result["data"][0]
                for key, value in row.items():
                    data_type = data_types.get(key, "scalar")
                    if data_type == "array" and isinstance(value, list):
                        tables.append({"name": key, "data": value})
                    elif data_type == "scalar":
                        cards.append({"label": key, "value": value})
            
            response = {
                "status": "success",
                "original_query": request.sql_query,
                "data": result["data"],
                "columns": result["columns"],
                "data_types": data_types,
                "row_count": len(result["data"]),
                "cards": cards,
                "tables": tables
            }
            
            if attempt > 0:
                response["retry_count"] = attempt
                response["final_query"] = current_query
                response["retry_token_usage"] = retry_token_usage
            
            return response
            
        except Exception as e:
            error_msg = str(e)
            print(f"Attempt {attempt + 1} failed: {error_msg}")
            
            # Last attempt - return error
            if attempt == max_retries - 1:
                raise HTTPException(status_code=500, detail=f"SQL execution failed after {max_retries} attempts: {error_msg}")
            
            # Try to fix with LLM
            try:
                print(f"Attempting LLM fix for attempt {attempt + 2}...")
                # Use filtered schema if available, otherwise full schema
                fix_schema = schema if schema else (db_instance.table_info if db_instance else "")
                if not fix_schema:
                    print("No schema available for fixing")
                    continue
                current_query, fix_tokens = query_engine.fix_sql_query(current_query, error_msg, fix_schema)
                retry_token_usage.append({
                    "attempt": attempt + 1,
                    "error": error_msg[:100],
                    "tokens": fix_tokens
                })
                print(f"Fixed query: {current_query}")
            except Exception as fix_error:
                print(f"LLM fix failed: {fix_error}")

def serialize_datetime(obj):
    """Serialize datetime objects"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj

def fix_column_casing(sql_query: str) -> str:
    """Lowercase mixed-case column references for PostgreSQL"""
    pattern = r'\b([a-z_][a-z0-9_]*)\\.([a-zA-Z_][a-zA-Z0-9_]*)\b'
    
    def lowercase_column(match):
        table = match.group(1)
        column = match.group(2)
        return f'{table}.{column.lower()}'
    
    return re.sub(pattern, lowercase_column, sql_query)

def categorize_columns(data, columns):
    """Categorize columns as scalar or array based on data"""
    data_types = {}
    for col in columns:
        is_array = any(isinstance(row.get(col), (list, dict)) for row in data)
        data_types[col] = "array" if is_array else "scalar"
    return data_types

def execute_sql_direct(sql_query: str, db_record: DBModel = None, plain_password: str = None):
    """Execute SQL directly on database"""
    if db_record is None:
        raise Exception("No database configuration available")
    if plain_password is None:
        raise Exception("Database password required")
    
    cleaned_query = sql_query.strip().replace("```sql", "").replace("```", "")
    
    statements = [s.strip() for s in cleaned_query.split(';') if s.strip()]
    if len(statements) > 1:
        cte_part = None
        select_part = None
        
        for stmt in statements:
            if stmt.upper().startswith('WITH'):
                cte_part = stmt
            elif stmt.upper().startswith('SELECT'):
                select_part = stmt
        
        if cte_part and select_part:
            cleaned_query = cte_part + ' ' + select_part
        elif select_part:
            cleaned_query = select_part
        else:
            cleaned_query = statements[-1]
    
    if cleaned_query.endswith(';'):
        cleaned_query = cleaned_query[:-1]
    
    if db_record.provider.value == "postgres":
        cleaned_query = fix_column_casing(cleaned_query)
    #postgres connection -----------------
    try:
        if db_record.provider.value == "postgres":
            conn = psycopg2.connect(
                host=db_record.host,
                port=db_record.port,
                database=db_record.db_name,
                user=db_record.user,
                password=plain_password
            )
            
            cursor = conn.cursor()
            cursor.execute(cleaned_query)
            
            columns = [desc[0] for desc in cursor.description] if cursor.description else []
            results = cursor.fetchall()
            
            data = []
            for row in results:
                if len(columns) > 0:
                    row_dict = {}
                    for col, val in zip(columns, row):
                        row_dict[col] = serialize_datetime(val)
                    data.append(row_dict)
                else:
                    data.append({"result": str(row)})
            
            cursor.close()
            conn.close()
            
            data_types = categorize_columns(data, columns)
            return {"data": data, "columns": columns if columns else ["result"], "data_types": data_types}
            
        elif db_record.provider.value == "mysql":
            conn = pymysql.connect(
                host=db_record.host,
                port=db_record.port,
                database=db_record.db_name,
                user=db_record.user,
                password=plain_password
            )
            
            cursor = conn.cursor()
            cursor.execute(cleaned_query)
            
            columns = [desc[0] for desc in cursor.description] if cursor.description else []
            results = cursor.fetchall()
            
            data = []
            for row in results:
                if len(columns) > 0:
                    row_dict = {}
                    for col, val in zip(columns, row):
                        row_dict[col] = serialize_datetime(val)
                    data.append(row_dict)
                else:
                    data.append({"result": str(row)})
            
            cursor.close()
            conn.close()
            
            data_types = categorize_columns(data, columns)
            return {"data": data, "columns": columns if columns else ["result"], "data_types": data_types}
            
        elif db_record.provider.value == "mssql":
            conn = pymssql.connect(
                server=db_record.host,
                port=db_record.port,
                database=db_record.db_name,
                user=db_record.user,
                password=plain_password
            )
            
            cursor = conn.cursor()
            cursor.execute(cleaned_query)
            
            columns = [desc[0] for desc in cursor.description] if cursor.description else []
            results = cursor.fetchall()
            
            data = []
            for row in results:
                if len(columns) > 0:
                    row_dict = {}
                    for col, val in zip(columns, row):
                        row_dict[col] = serialize_datetime(val)
                    data.append(row_dict)
                else:
                    data.append({"result": str(row)})
            
            cursor.close()
            conn.close()
            
            data_types = categorize_columns(data, columns)
            return {"data": data, "columns": columns if columns else ["result"], "data_types": data_types}
            
    except Exception as e:
        raise Exception(f"SQL execution failed: {str(e)}")

@router.get("/health")
async def health_check():
    """System health check"""
    memory_status = None
    if query_engine:
        memory_status = {
            "session_id": query_engine.memory.session_id,
            "messages_stored": len(query_engine.memory.messages),
            "token_estimate": query_engine.memory.get_token_estimate(),
            "max_exchanges": query_engine.memory.max_exchanges
        }
    
    return {
        "status": "healthy",
        "service": "NLP-to-SQL with Conversation Memory",
        "database_connected": current_db is not None,
        "query_engine_ready": query_engine is not None,
        "memory_status": memory_status,
        "features": [
            "SQL Query Generation",
            "Intent Classification",
            "Web Search Integration",
            "Conversation Memory (5 exchanges)",
            "Smart Token Optimization",
            "Context-Aware Query Resolution"
        ],
        "endpoints": {
            "/database/connect": "Connect database with session ID",
            "/database/query": "NLP query with memory",
            "/database/query-and-execute": "Generate & execute SQL",
            "/database/conversation/history": "Get conversation history",
            "/database/conversation/clear": "Clear conversation",
            "/database/conversation/stats": "Memory statistics",
            "/database/test-intent": "Test intent classification",
            "/database/health": "Health check"
        }
    }

@router.get("/stats")
async def get_system_stats():
    """Get detailed system statistics"""
    if current_db is None or query_engine is None:
        return {
            "status": "not_initialized",
            "message": "Database not connected"
        }
    
    try:
        table_names = current_db.get_usable_table_names()
        memory = query_engine.memory
        
        return {
            "status": "operational",
            "database": {
                "type": current_db_config.db_type if current_db_config else "unknown",
                "connected": True,
                "table_count": len(table_names),
                "tables": table_names
            },
            "query_engine": {
                "initialized": True,
                "csv_catalog": current_csv_path,
                "llm_model": "llama-3.3-70b-versatile"
            },
            "memory": {
                "session_id": memory.session_id,
                "session_created": memory.created_at.isoformat(),
                "total_messages": len(memory.messages),
                "token_estimate": memory.get_token_estimate(),
                "max_exchanges": memory.max_exchanges,
                "max_tokens_per_message": memory.max_tokens_per_msg,
                "memory_utilization": f"{(len(memory.messages) // 2) / memory.max_exchanges * 100:.1f}%"
            }
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}
