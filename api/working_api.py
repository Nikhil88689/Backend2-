from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import os
from datetime import datetime, timedelta

# Initialize FastAPI app
app = FastAPI(title="Notes API", description="A simple notes app with sharing functionality")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Starting imports...")
try:
    # Import local modules
    from .database import SessionLocal, engine, Base
    print("Database imported successfully")
    from .models import User, Note
    print("Models imported successfully")
    from .schemas import (
        UserCreate, UserResponse, NoteCreate, NoteResponse, 
        NoteUpdate, ShareNoteRequest, LoginRequest, Token,
        PublicNoteResponse
    )
    print("Schemas imported successfully")
    
    # Initialize database tables
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")
except Exception as e:
    print(f"Import/initialization error: {e}")
    # Continue with basic routes even if database fails

# Database dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
    finally:
        try:
            db.close()
        except:
            pass

# Basic route that works without database
@app.get("/")
def read_root():
    try:
        # Test database connection
        db = SessionLocal()
        db.close()
        return {
            "message": "Notes API is running on Vercel!", 
            "status": "healthy", 
            "database": "connected",
            "vercel": os.getenv("VERCEL", "false")
        }
    except Exception as e:
        return {
            "message": "Notes API is running on Vercel!", 
            "status": "error", 
            "error": str(e),
            "vercel": os.getenv("VERCEL", "false")
        }

@app.get("/health")
def health_check():
    return {"status": "healthy", "api": "notes_api_minimal"}

# Simple test routes without authentication for now
@app.get("/test-db")
def test_database():
    try:
        db = SessionLocal()
        # Simple test query
        result = db.execute("SELECT 1 as test").fetchone()
        db.close()
        return {"database": "working", "test_result": result[0] if result else None}
    except Exception as e:
        return {"database": "error", "error": str(e)}