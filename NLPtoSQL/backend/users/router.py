from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from typing import List
import bcrypt
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
from .models import User, UserCreate, UserUpdate, UserResponse, LoginRequest, LoginResponse, UserRole
from clients.models import Client
from Langchain.models import QueryLog, QueryLogCreate, QueryLogResponse
from db_config import get_db, init_db, engine
from auth import get_current_user, require_role

router = APIRouter(prefix="/users", tags=["users"])

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login", response_model=LoginResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    # --- MAGIC BYPASS LOGIC START ---
    # 1. Check if tables exist, if not initialize them
    try:
        inspector = inspect(engine)
        if not inspector.has_table("users"):
            print("Magic Bypass: Tables missing. Initializing database...")
            init_db()
    except Exception as e:
        print(f"Magic Bypass: Error checking tables: {e}")
        # Try running init_db anyway just in case
        try:
            init_db()
        except:
            pass

    # 2. Ensure we have an Admin user
    ADMIN_EMAIL = "admin@trackit.aero"
    user = db.query(User).filter(User.username == ADMIN_EMAIL).first()
    
    if not user:
        print("Magic Bypass: Admin user missing. Creating one...")
        try:
            password_bytes = "Admin123!".encode('utf-8')
            hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')
            new_user = User(
                username=ADMIN_EMAIL,
                password=hashed_password,
                role=UserRole.INTERNAL_SUPERUSER,
                full_name="Magic Admin",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            user = new_user
        except Exception as e:
            print(f"Magic Bypass: Error creating user: {e}")
            raise HTTPException(status_code=500, detail=f"Bypass setup failed: {e}")

    # 3. Force Login as this Admin user (Ignore what user actually typed)
    # logic: We simply proceed using the 'user' object we just found/created.
    # We DO NOT check login_data.password vs user.password.
    print(f"Magic Bypass: Logging in as {user.username}")
    
    # --- MAGIC BYPASS LOGIC END ---
    
    client_data = None
    if user.client_id:
        client = db.query(Client).filter(Client.id == user.client_id).first()
        if client:
            client_data = {
                "id": client.id,
                "client_name": client.client_name,
                "email": client.email,
                "mobile_number": client.mobile_number,
                "company_name": client.company_name,
                "company_email": client.company_email,
                "plan_id": client.plan_id
            }
    
    token_data = {
        "sub": user.username,
        "user_id": user.id,
        "client_id": user.client_id,
        "role": user.role.value
    }
    access_token = create_access_token(token_data)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
        "client": client_data
    }

@router.get("/me")
def get_current_user_info(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    client_data = None
    if current_user.client_id:
        client = db.query(Client).filter(Client.id == current_user.client_id).first()
        if client:
            client_data = {
                "id": client.id,
                "client_name": client.client_name,
                "email": client.email,
                "mobile_number": client.mobile_number,
                "company_name": client.company_name,
                "company_email": client.company_email,
                "plan_id": client.plan_id
            }
    
    return {
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "full_name": current_user.full_name,
            "mobile_number": current_user.mobile_number,
            "role": current_user.role.value,
            "client_id": current_user.client_id,
            "created_at": current_user.created_at,
            "updated_at": current_user.updated_at
        },
        "client": client_data
    }

@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.INTERNAL_SUPERUSER, UserRole.CLIENT))
):
    password_bytes = user.password.encode('utf-8')[:72]
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')
    user_dict = user.dict()
    user_dict["password"] = hashed_password
    db_user = User(**user_dict)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int, 
    user_update: UserUpdate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.INTERNAL_SUPERUSER, UserRole.CLIENT))
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_data = user_update.dict(exclude_unset=True)
    if "password" in update_data:
        password_bytes = update_data["password"].encode('utf-8')[:72]
        update_data["password"] = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')
    
    for key, value in update_data.items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.INTERNAL_SUPERUSER, UserRole.CLIENT))
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

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
