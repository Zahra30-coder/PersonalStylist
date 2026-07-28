from fastapi import FastAPI
from app.middleware.request_id import RequestIDMiddleware
from app.routes.user_routes import router
from app import models
from app.models import db_models
from app.connection.db import engine
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# Create tables
db_models.Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
async def root():
    return {"Start Exploring Our in-house Fashion App!"}

@app.get("/api/health")
async def health():
    return {"status": "OK"}

# Create tables
db_models.Base.metadata.create_all(
    bind=engine
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)