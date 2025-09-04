from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# For Vercel serverless deployment, use SQLite in /tmp directory
if os.getenv("VERCEL"):
    # Ensure /tmp directory exists
    os.makedirs("/tmp", exist_ok=True)
    SQLALCHEMY_DATABASE_URL = "sqlite:////tmp/notes.db"
else:
    # For local development, use SQLite only (no PostgreSQL support in serverless)
    SQLALCHEMY_DATABASE_URL = "sqlite:///./notes.db"

print(f"Using database URL: {SQLALCHEMY_DATABASE_URL}")

# Configure engine - always use SQLite for serverless
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()