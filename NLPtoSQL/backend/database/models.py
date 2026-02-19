from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Text, Enum as SQLEnum
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum
from models import Base

class DBProvider(str, Enum):
    MYSQL = "mysql"
    POSTGRES = "postgres"
    MSSQL = "mssql"

class Database(Base):
    __tablename__ = "databases"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    provider = Column(SQLEnum(DBProvider), nullable=False)
    port = Column(Integer, nullable=False)
    host = Column(String(255), nullable=False)
    user = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    db_name = Column(String(255), nullable=False)
    description = Column(JSON, nullable=True)
    db_description = Column(Text, nullable=True)
    title = Column(String(255), nullable=True)
    private_columns = Column(JSON, nullable=True)
    selected_tables = Column(JSON, nullable=True)
    schema = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class DatabaseBase(BaseModel):
    provider: DBProvider
    port: int
    host: str
    user: str
    password: str
    db_name: str
    title: Optional[str] = None
    description: Optional[Dict[str, Any]] = None
    db_description: Optional[str] = None
    private_columns: Optional[Dict[str, Any]] = None
    selected_tables: Optional[List[str]] = None
    schema: Optional[Dict[str, Any]] = None

class DatabaseCreate(DatabaseBase):
    client_id: Optional[int] = None

class DatabaseUpdate(BaseModel):
    provider: Optional[DBProvider] = None
    port: Optional[int] = None
    host: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None
    db_name: Optional[str] = None
    description: Optional[Dict[str, Any]] = None
    db_description: Optional[str] = None
    private_columns: Optional[Dict[str, Any]] = None
    selected_tables: Optional[List[str]] = None
    schema: Optional[Dict[str, Any]] = None
    title: Optional[str] = None

class DatabaseResponse(BaseModel):
    id: int
    client_id: int
    provider: DBProvider
    port: int
    host: str
    user: str
    db_name: str
    description: Optional[Dict[str, Any]] = None #Description metadata about the database tables
    db_description: Optional[str] = None #Data base description
    private_columns: Optional[Dict[str, Any]] = None
    selected_tables: Optional[List[str]] = None
    schema: Optional[Dict[str, Any]] = None #Cached schema structure
    created_at: datetime
    updated_at: Optional[datetime] = None
    title: Optional[str] = None
    
    class Config:
        from_attributes = True

class DatabaseTestConnection(BaseModel):
    provider: DBProvider
    port: int
    host: str
    user: str
    password: str
    db_name: str

class GetTablesViewsRequest(BaseModel):
    provider: DBProvider
    port: int
    host: str
    user: str
    password: str
    db_name: str
    schemas: List[str]

class GenerateSchemaRequest(BaseModel):
    provider: DBProvider
    port: int
    host: str
    user: str
    password: str
    db_name: str
    selected_tables: List[str]
