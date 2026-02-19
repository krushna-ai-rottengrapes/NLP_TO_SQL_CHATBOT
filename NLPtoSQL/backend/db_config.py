from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/nlptosql")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # Checks if connection is alive before using it
    pool_size=10,         # Keeps 10 connections open
    max_overflow=20,      # Allows 20 extra if needed
    pool_recycle=300      # Recycles connections every 5 minutes to prevent stale timeouts
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    # Import all models to register them with Base
    from clients.models import Client, Plan
    from database.models import Database
    from users.models import User
    from dashboards.models import SavedDashboard
    from Langchain.models import QueryLog
    
    Base.metadata.create_all(bind=engine)
