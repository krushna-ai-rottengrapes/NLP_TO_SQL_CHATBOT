from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .models import SavedDashboard, SavedDashboardCreate, SavedDashboardUpdate, SavedDashboardResponse
from clients.models import Plan, PlanCreate, PlanUpdate, PlanResponse
from db_config import get_db
from auth import get_current_user
from users.models import User, UserRole

# Saved Dashboards
dashboard_router = APIRouter(prefix="/dashboards", tags=["dashboards"])

@dashboard_router.post("/", response_model=SavedDashboardResponse)
def create_dashboard(dashboard: SavedDashboardCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_dashboard = SavedDashboard(**dashboard.dict())
    db.add(db_dashboard)
    db.commit()
    db.refresh(db_dashboard)
    return db_dashboard

@dashboard_router.get("/", response_model=List[SavedDashboardResponse])
def get_dashboards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(SavedDashboard).offset(skip).limit(limit).all()

@dashboard_router.get("/client/{client_id}", response_model=List[SavedDashboardResponse])
def get_dashboards_by_client(client_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(SavedDashboard).filter(SavedDashboard.client_id == client_id).all()

@dashboard_router.get("/{dashboard_id}", response_model=SavedDashboardResponse)
def get_dashboard(dashboard_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    dashboard = db.query(SavedDashboard).filter(SavedDashboard.id == dashboard_id).first()
    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    return dashboard

@dashboard_router.put("/{dashboard_id}", response_model=SavedDashboardResponse)
def update_dashboard(dashboard_id: int, dashboard_update: SavedDashboardUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    dashboard = db.query(SavedDashboard).filter(SavedDashboard.id == dashboard_id).first()
    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    
    update_data = dashboard_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(dashboard, key, value)
    
    db.commit()
    db.refresh(dashboard)
    return dashboard

@dashboard_router.delete("/{dashboard_id}")
def delete_dashboard(dashboard_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    dashboard = db.query(SavedDashboard).filter(SavedDashboard.id == dashboard_id).first()
    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    
    if current_user.role != UserRole.INTERNAL_SUPERUSER and dashboard.client_id != current_user.client_id:
        raise HTTPException(status_code=403, detail="Access denied")
    
    db.delete(dashboard)
    db.commit()
    return {"message": "Dashboard deleted successfully"}

# Plans
plan_router = APIRouter(prefix="/plans", tags=["plans"])

@plan_router.post("/", response_model=PlanResponse)
def create_plan(plan: PlanCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_plan = Plan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

@plan_router.get("/", response_model=List[PlanResponse])
def get_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Plan).offset(skip).limit(limit).all()

@plan_router.get("/{plan_id}", response_model=PlanResponse)
def get_plan(plan_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@plan_router.put("/{plan_id}", response_model=PlanResponse)
def update_plan(plan_id: int, plan_update: PlanUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    for key, value in plan_update.dict(exclude_unset=True).items():
        setattr(plan, key, value)
    
    db.commit()
    db.refresh(plan)
    return plan

@plan_router.delete("/{plan_id}")
def delete_plan(plan_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    db.delete(plan)
    db.commit()
    return {"message": "Plan deleted successfully"}
