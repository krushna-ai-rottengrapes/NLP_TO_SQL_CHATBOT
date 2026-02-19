from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import initialize_db_connection, router as database_router
from database.router import router as db_config_router
from clients.router import router as client_router
from users.router import router as user_router, query_router
from dashboards.router import dashboard_router, plan_router
from db_config import init_db

app = FastAPI(title="NLP to SQL API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    init_db()
    initialize_db_connection()

app.include_router(database_router)
app.include_router(client_router)
app.include_router(db_config_router)
app.include_router(user_router)
app.include_router(query_router)
app.include_router(dashboard_router)
app.include_router(plan_router)

@app.get("/")
def read_root():
    return {"message": "NLP to SQL API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)