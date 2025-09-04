from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# For Vercel serverless deployment, use SQLite in /tmp directory
if os.getenv("VERCEL"):
    SQLALCHEMY_DATABASE_URL = "sqlite:////tmp/notes.db"
else:
    # Use environment variable for database URL, fallback to local SQLite
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./notes.db")

# Configure engine based on database type
if SQLALCHEMY_DATABASE_URL.startswith("postgresql"):
    # PostgreSQL configuration for production
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_pre_ping=True,
        pool_recycle=300,
        connect_args={
            "sslmode": "require",
            "connect_timeout": 10
        }
    )
else:
    # SQLite configuration for local development and Vercel
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, 
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()