from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from models import Base

# SQLAlchemy Models
class Plan(Base):
    __tablename__ = "plans"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    total_query_allowed = Column(Integer, nullable=False)
    tokens = Column(Integer, nullable=True)
    users = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(255), nullable=False)
    mobile_number = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    company_name = Column(String(255), nullable=True)
    company_address = Column(Text, nullable=True)
    company_field = Column(String(255), nullable=True)
    company_logo = Column(String(500), nullable=True)
    company_email = Column(String(255), nullable=True)
    company_pan = Column(String(50), nullable=True)
    plan_id = Column(Integer, ForeignKey("plans.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

# Pydantic Schemas
class PlanBase(BaseModel):
    name: str
    total_query_allowed: Optional[int] = None
    tokens: Optional[int] = None
    users: Optional[int] = None

class PlanCreate(PlanBase):
    pass

class PlanUpdate(BaseModel):
    name: Optional[str] = None
    total_query_allowed: Optional[int] = None
    tokens: Optional[int] = None
    users: Optional[int] = None

class PlanResponse(PlanBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class ClientBase(BaseModel):
    client_name: str
    mobile_number: str
    email: EmailStr
    company_name: Optional[str] = None
    company_address: Optional[str] = None
    company_field: Optional[str] = None
    company_logo: Optional[str] = None
    company_email: Optional[EmailStr] = None
    company_pan: Optional[str] = None
    plan_id: Optional[int] = None

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    client_name: Optional[str] = None
    mobile_number: Optional[str] = None
    email: Optional[EmailStr] = None
    company_name: Optional[str] = None
    company_address: Optional[str] = None
    company_field: Optional[str] = None
    company_logo: Optional[str] = None
    company_email: Optional[EmailStr] = None
    company_pan: Optional[str] = None
    plan_id: Optional[int] = None

class ClientResponse(ClientBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
