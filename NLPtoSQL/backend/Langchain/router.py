from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from .models import User, UserCreate, UserUpdate, UserResponse, SavedDashboard, SavedDashboardCreate, SavedDashboardUpdate, SavedDashboardResponse
from clients.models import Plan, PlanCreate, PlanUpdate, PlanResponse
from Langchain.models import QueryLog, QueryLogCreate, QueryLogResponse
from db_config import get_db



# Query Logs
query_router = APIRouter(prefix="/query-logs", tags=["query-logs"])

@query_router.post("/", response_model=QueryLogResponse)
def create_query_log(query_log: QueryLogCreate, db: Session = Depends(get_db)):
    db_query_log = QueryLog(**query_log.dict())
    db.add(db_query_log)
    db.commit()
    db.refresh(db_query_log)
    return db_query_log

@query_router.get("/", response_model=List[QueryLogResponse])
def get_query_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(QueryLog).offset(skip).limit(limit).all()

@query_router.get("/client/{client_id}", response_model=List[QueryLogResponse])
def get_query_logs_by_client(client_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(QueryLog).filter(QueryLog.client_id == client_id).offset(skip).limit(limit).all()

@query_router.get("/{query_log_id}", response_model=QueryLogResponse)
def get_query_log(query_log_id: int, db: Session = Depends(get_db)):
    query_log = db.query(QueryLog).filter(QueryLog.id == query_log_id).first()
    if not query_log:
        raise HTTPException(status_code=404, detail="Query log not found")
    return query_log

# Saved Dashboards
dashboard_router = APIRouter(prefix="/dashboards", tags=["dashboards"])

@dashboard_router.post("/", response_model=SavedDashboardResponse)
def create_dashboard(dashboard: SavedDashboardCreate, db: Session = Depends(get_db)):
    db_dashboard = SavedDashboard(**dashboard.dict())
    db.add(db_dashboard)
    db.commit()
    db.refresh(db_dashboard)
    return db_dashboard

@dashboard_router.get("/", response_model=List[SavedDashboardResponse])
def get_dashboards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(SavedDashboard).offset(skip).limit(limit).all()

@dashboard_router.get("/client/{client_id}", response_model=List[SavedDashboardResponse])
def get_dashboards_by_client(client_id: int, db: Session = Depends(get_db)):
    return db.query(SavedDashboard).filter(SavedDashboard.client_id == client_id).all()

@dashboard_router.get("/{dashboard_id}", response_model=SavedDashboardResponse)
def get_dashboard(dashboard_id: int, db: Session = Depends(get_db)):
    dashboard = db.query(SavedDashboard).filter(SavedDashboard.id == dashboard_id).first()
    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    return dashboard

@dashboard_router.put("/{dashboard_id}", response_model=SavedDashboardResponse)
def update_dashboard(dashboard_id: int, dashboard_update: SavedDashboardUpdate, db: Session = Depends(get_db)):
    dashboard = db.query(SavedDashboard).filter(SavedDashboard.id == dashboard_id).first()
    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    
    for key, value in dashboard_update.dict(exclude_unset=True).items():
        setattr(dashboard, key, value)
    
    db.commit()
    db.refresh(dashboard)
    return dashboard

@dashboard_router.delete("/{dashboard_id}")
def delete_dashboard(dashboard_id: int, db: Session = Depends(get_db)):
    dashboard = db.query(SavedDashboard).filter(SavedDashboard.id == dashboard_id).first()
    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    
    db.delete(dashboard)
    db.commit()
    return {"message": "Dashboard deleted successfully"}

# Plans
plan_router = APIRouter(prefix="/plans", tags=["plans"])

@plan_router.post("/", response_model=PlanResponse)
def create_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    db_plan = Plan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

@plan_router.get("/", response_model=List[PlanResponse])
def get_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Plan).offset(skip).limit(limit).all()

@plan_router.get("/{plan_id}", response_model=PlanResponse)
def get_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@plan_router.put("/{plan_id}", response_model=PlanResponse)
def update_plan(plan_id: int, plan_update: PlanUpdate, db: Session = Depends(get_db)):
    plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    for key, value in plan_update.dict(exclude_unset=True).items():
        setattr(plan, key, value)
    
    db.commit()
    db.refresh(plan)
    return plan

@plan_router.delete("/{plan_id}")
def delete_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    db.delete(plan)
    db.commit()
    return {"message": "Plan deleted successfully"}
