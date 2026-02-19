from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from models import Base

class SavedDashboard(Base):
    __tablename__ = "saved_dashboards"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    db_id = Column(Integer, nullable=True)
    db_name = Column(String(255), nullable=True)
    chats = Column(JSON, nullable=True)
    charts = Column(JSON, nullable=True)
    title = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class SavedDashboardBase(BaseModel):
    client_id: int
    db_id: Optional[int] = None
    db_name: Optional[str] = None
    chats: Optional[List[Dict[str, Any]]] = None
    charts: Optional[List[Dict[str, Any]]] = None
    title: Optional[str] = None

class SavedDashboardCreate(SavedDashboardBase):
    pass

class SavedDashboardUpdate(BaseModel):
    db_id: Optional[int] = None
    db_name: Optional[str] = None
    chats: Optional[List[Dict[str, Any]]] = None
    charts: Optional[List[Dict[str, Any]]] = None
    title: Optional[str] = None

class SavedDashboardResponse(SavedDashboardBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
