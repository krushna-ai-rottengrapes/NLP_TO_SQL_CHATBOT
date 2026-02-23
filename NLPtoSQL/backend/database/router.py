from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import psycopg2
import pymysql
import pymssql
from .models import Database, DatabaseCreate, DatabaseUpdate, DatabaseResponse, DatabaseTestConnection, GetTablesViewsRequest, GenerateSchemaRequest
from db_config import get_db
from auth import get_current_user
from users.models import User, UserRole
from utils.encryption import encrypt_password, decrypt_password

router = APIRouter(prefix="/databases", tags=["databases"])

@router.post("/", response_model=DatabaseResponse)
def create_database(
    database: DatabaseCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role == UserRole.CLIENT_USER:
        raise HTTPException(status_code=403, detail="Client users cannot create databases")
    
    if current_user.role == UserRole.INTERNAL_SUPERUSER:
        if not database.client_id:
            raise HTTPException(status_code=400, detail="client_id is required for superuser")
    else:
        database.client_id = current_user.client_id
    
    db_dict = database.dict()
    db_dict["host"] = db_dict["host"].strip()
    db_dict["db_name"] = db_dict["db_name"].strip()
    db_dict["user"] = db_dict["user"].strip()
    db_dict["password"] = encrypt_password(db_dict["password"])
    
    db_database = Database(**db_dict)
    db.add(db_database)
    db.commit()
    db.refresh(db_database)
    return db_database

@router.get("/", response_model=List[DatabaseResponse])
def get_databases(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role == UserRole.INTERNAL_SUPERUSER:
        return db.query(Database).offset(skip).limit(limit).all()
    return db.query(Database).filter(Database.client_id == current_user.client_id).offset(skip).limit(limit).all()

@router.get("/client/{client_id}", response_model=List[DatabaseResponse])
def get_databases_by_client(
    client_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.INTERNAL_SUPERUSER and current_user.client_id != client_id:
        raise HTTPException(status_code=403, detail="Access denied")
    return db.query(Database).filter(Database.client_id == client_id).all()

@router.get("/{database_id}", response_model=DatabaseResponse)
def get_database(
    database_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    database = db.query(Database).filter(Database.id == database_id).first()
    if not database:
        raise HTTPException(status_code=404, detail="Database not found")
    
    if current_user.role != UserRole.INTERNAL_SUPERUSER and database.client_id != current_user.client_id:
        raise HTTPException(status_code=403, detail="Access denied")
    return database

@router.put("/{database_id}", response_model=DatabaseResponse)
def update_database(
    database_id: int, 
    database_update: DatabaseUpdate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    database = db.query(Database).filter(Database.id == database_id).first()
    if not database:
        raise HTTPException(status_code=404, detail="Database not found")
    
    if current_user.role != UserRole.INTERNAL_SUPERUSER and database.client_id != current_user.client_id:
        raise HTTPException(status_code=403, detail="Access denied")
    
    update_data = database_update.dict(exclude_unset=True)
    if "password" in update_data:
        update_data["password"] = encrypt_password(update_data["password"])
    
    # If description is being updated, sync selected_tables with description keys
    if "description" in update_data and update_data["description"]:
        description_tables = list(update_data["description"].keys())
        update_data["selected_tables"] = description_tables
    
    for key, value in update_data.items():
        setattr(database, key, value)
    
    db.commit()
    db.refresh(database)
    return database

@router.delete("/{database_id}")
def delete_database(
    database_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    database = db.query(Database).filter(Database.id == database_id).first()
    if not database:
        raise HTTPException(status_code=404, detail="Database not found")
    
    if current_user.role != UserRole.INTERNAL_SUPERUSER and database.client_id != current_user.client_id:
        raise HTTPException(status_code=403, detail="Access denied")
    
    db.delete(database)
    db.commit()
    return {"message": "Database deleted successfully"}

@router.post("/test-connection")
def test_database_connection(
    config: DatabaseTestConnection,
    current_user: User = Depends(get_current_user)
):
    try:
        host = config.host.strip()
        db_name = config.db_name.strip()
        user = config.user.strip()
        plain_password = config.password.strip()
        
        if config.provider == "postgres":
            conn = psycopg2.connect(
                host=host,
                port=config.port,
                database=db_name,
                user=user,
                password=plain_password,
                connect_timeout=5
            )
            cursor = conn.cursor()
            cursor.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('pg_catalog', 'information_schema', 'pg_toast')")
            schemas = [row[0] for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            
            return {
                "status": "success",
                "message": "Connection successful",
                "schemas": schemas
            }
            
        elif config.provider == "mysql":
            conn = pymysql.connect(
                host=host,
                port=config.port,
                database=db_name,
                user=user,
                password=plain_password,
                connect_timeout=5
            )
            cursor = conn.cursor()
            cursor.execute("SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')")
            schemas = [row[0] for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            
            return {
                "status": "success",
                "message": "Connection successful",
                "schemas": schemas
            }
            
        elif config.provider == "mssql":
            conn = pymssql.connect(
                server=host,
                port=config.port,
                database=db_name,
                user=user,
                password=plain_password,
                timeout=5
            )
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sys.schemas WHERE name NOT IN ('guest', 'INFORMATION_SCHEMA', 'sys', 'db_owner', 'db_accessadmin', 'db_securityadmin', 'db_ddladmin', 'db_backupoperator', 'db_datareader', 'db_datawriter', 'db_denydatareader', 'db_denydatawriter')")
            schemas = [row[0] for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            
            return {
                "status": "success",
                "message": "Connection successful",
                "schemas": schemas
            }
        else:
            raise HTTPException(status_code=400, detail="Unsupported database provider")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Connection failed: {str(e)}")

@router.post("/get-tables-views")
def get_tables_and_views(
    request: GetTablesViewsRequest,
    current_user: User = Depends(get_current_user)
):
    try:
        host = request.host.strip()
        db_name = request.db_name.strip()
        user = request.user.strip()
        plain_password = request.password.strip()
        schemas = request.schemas
        
        if request.provider == "postgres":
            conn = psycopg2.connect(
                host=host,
                port=request.port,
                database=db_name,
                user=user,
                password=plain_password,
                connect_timeout=5
            )
            cursor = conn.cursor()
            schema_list = "', '".join(schemas)
            cursor.execute(f"""
                -- Get regular tables and views
                SELECT table_schema, table_name, table_type 
                FROM information_schema.tables 
                WHERE table_schema IN ('{schema_list}')
                
                UNION ALL
                
                -- Get materialized views
                SELECT schemaname, matviewname, 'MATERIALIZED VIEW'
                FROM pg_matviews 
                WHERE schemaname IN ('{schema_list}')
                
                ORDER BY 1, 2
            """)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            
            tables_views = []
            for schema, name, ttype in results:
                tables_views.append({
                    "schema": schema,
                    "name": name,
                    "full_name": f"{schema}.{name}",
                    "type": "materialized_view" if ttype == "MATERIALIZED VIEW" else ("view" if ttype == "VIEW" else "table")
                })
            
            return {
                "status": "success",
                "tables_views": tables_views
            }
            
        elif request.provider == "mysql":
            conn = pymysql.connect(
                host=host,
                port=request.port,
                database=db_name,
                user=user,
                password=plain_password,
                connect_timeout=5
            )
            cursor = conn.cursor()
            schema_list = "', '".join(schemas)
            cursor.execute(f"""
                SELECT TABLE_SCHEMA, TABLE_NAME, TABLE_TYPE 
                FROM information_schema.TABLES 
                WHERE TABLE_SCHEMA IN ('{schema_list}')
                ORDER BY TABLE_SCHEMA, TABLE_NAME
            """)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            
            tables_views = []
            for schema, name, ttype in results:
                tables_views.append({
                    "schema": schema,
                    "name": name,
                    "full_name": f"{schema}.{name}",
                    "type": "view" if ttype == "VIEW" else "table"
                })
            
            return {
                "status": "success",
                "tables_views": tables_views
            }
            
        elif request.provider == "mssql":
            conn = pymssql.connect(
                server=host,
                port=request.port,
                database=db_name,
                user=user,
                password=plain_password,
                timeout=5
            )
            cursor = conn.cursor()
            schema_list = "', '".join(schemas)
            cursor.execute(f"""
                SELECT TABLE_SCHEMA, TABLE_NAME, TABLE_TYPE 
                FROM INFORMATION_SCHEMA.TABLES 
                WHERE TABLE_SCHEMA IN ('{schema_list}')
                ORDER BY TABLE_SCHEMA, TABLE_NAME
            """)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            
            tables_views = []
            for schema, name, ttype in results:
                tables_views.append({
                    "schema": schema,
                    "name": name,
                    "full_name": f"{schema}.{name}",
                    "type": "view" if ttype == "VIEW" else "table"
                })
            
            return {
                "status": "success",
                "tables_views": tables_views
            }
        else:
            raise HTTPException(status_code=400, detail="Unsupported database provider")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch tables/views: {str(e)}")

@router.post("/generate-schema")
def generate_schema(
    request: GenerateSchemaRequest,
    current_user: User = Depends(get_current_user)
):
    try:
        host = request.host.strip()
        db_name = request.db_name.strip()
        user = request.user.strip()
        plain_password = request.password.strip()
        selected_tables = request.selected_tables
        
        schema_data = {}
        
        if request.provider == "postgres":
            conn = psycopg2.connect(
                host=host,
                port=request.port,
                database=db_name,
                user=user,
                password=plain_password,
                connect_timeout=5
            )
            cursor = conn.cursor()
            
            for full_table in selected_tables:
                schema_name, table_name = full_table.split('.')
                cursor.execute(f"""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_schema = '{schema_name}' AND table_name = '{table_name}'
                    ORDER BY ordinal_position
                """)
                columns = [{"column": col, "type": dtype} for col, dtype in cursor.fetchall()]
                schema_data[full_table] = columns
            
            cursor.close()
            conn.close()
            
        elif request.provider == "mysql":
            conn = pymysql.connect(
                host=host,
                port=request.port,
                database=db_name,
                user=user,
                password=plain_password,
                connect_timeout=5
            )
            cursor = conn.cursor()
            
            for full_table in selected_tables:
                schema_name, table_name = full_table.split('.')
                cursor.execute(f"""
                    SELECT COLUMN_NAME, DATA_TYPE 
                    FROM information_schema.COLUMNS 
                    WHERE TABLE_SCHEMA = '{schema_name}' AND TABLE_NAME = '{table_name}'
                    ORDER BY ORDINAL_POSITION
                """)
                columns = [{"column": col, "type": dtype} for col, dtype in cursor.fetchall()]
                schema_data[full_table] = columns
            
            cursor.close()
            conn.close()
            
        elif request.provider == "mssql":
            conn = pymssql.connect(
                server=host,
                port=request.port,
                database=db_name,
                user=user,
                password=plain_password,
                timeout=5
            )
            cursor = conn.cursor()
            
            for full_table in selected_tables:
                schema_name, table_name = full_table.split('.')
                cursor.execute(f"""
                    SELECT COLUMN_NAME, DATA_TYPE 
                    FROM INFORMATION_SCHEMA.COLUMNS 
                    WHERE TABLE_SCHEMA = '{schema_name}' AND TABLE_NAME = '{table_name}'
                    ORDER BY ORDINAL_POSITION
                """)
                columns = [{"column": col, "type": dtype} for col, dtype in cursor.fetchall()]
                schema_data[full_table] = columns
            
            cursor.close()
            conn.close()
        
        return {
            "status": "success",
            "schema": schema_data
        }
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate schema: {str(e)}")

@router.get("/{database_id}/metadata")
def get_database_metadata(
    database_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    database = db.query(Database).filter(Database.id == database_id).first()
    if not database:
        raise HTTPException(status_code=404, detail="Database not found")
    
    if current_user.role != UserRole.INTERNAL_SUPERUSER and database.client_id != current_user.client_id:
        raise HTTPException(status_code=403, detail="Access denied")
    
    # Get plain password from user_db_store if connected
    if current_user.id not in user_db_store:
        raise HTTPException(status_code=503, detail="Database not connected. Please connect first.")
    
    plain_password = user_db_store[current_user.id].get("plain_password")
    if not plain_password:
        raise HTTPException(status_code=503, detail="Database password not available")
    
    try:
        if database.provider == "postgres":
            conn = psycopg2.connect(
                host=database.host,
                port=database.port,
                database=database.db_name,
                user=database.user,
                password=plain_password,
                connect_timeout=5
            )
            cursor = conn.cursor()
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = [row[0] for row in cursor.fetchall()]
            
            cursor.execute("""
                SELECT table_name, column_name, data_type 
                FROM information_schema.columns 
                WHERE table_schema = 'public'
                ORDER BY table_name, ordinal_position
            """)
            schema = {}
            for table, column, dtype in cursor.fetchall():
                if table not in schema:
                    schema[table] = []
                schema[table].append({"column": column, "type": dtype})
            
            cursor.close()
            conn.close()
            
            return {
                "status": "success",
                "tables": tables,
                "schema": schema
            }
            
        elif database.provider == "mysql":
            conn = pymysql.connect(
                host=database.host,
                port=database.port,
                database=database.db_name,
                user=database.user,
                password=plain_password,
                connect_timeout=5
            )
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = [row[0] for row in cursor.fetchall()]
            
            schema = {}
            for table in tables:
                cursor.execute(f"DESCRIBE {table}")
                schema[table] = [{"column": row[0], "type": row[1]} for row in cursor.fetchall()]
            
            cursor.close()
            conn.close()
            
            return {
                "status": "success",
                "tables": tables,
                "schema": schema
            }
            
        elif database.provider == "mssql":
            conn = pymssql.connect(
                server=database.host,
                port=database.port,
                database=database.db_name,
                user=database.user,
                password=plain_password,
                timeout=5
            )
            cursor = conn.cursor()
            cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
            tables = [row[0] for row in cursor.fetchall()]
            
            cursor.execute("""
                SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE 
                FROM INFORMATION_SCHEMA.COLUMNS 
                ORDER BY TABLE_NAME, ORDINAL_POSITION
            """)
            schema = {}
            for table, column, dtype in cursor.fetchall():
                if table not in schema:
                    schema[table] = []
                schema[table].append({"column": column, "type": dtype})
            
            cursor.close()
            conn.close()
            
            return {
                "status": "success",
                "tables": tables,
                "schema": schema
            }
        else:
            raise HTTPException(status_code=400, detail="Unsupported database provider")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch metadata: {str(e)}")
