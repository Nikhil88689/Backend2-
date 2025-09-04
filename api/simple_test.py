from fastapi import FastAPI
import os

app = FastAPI(title="Simple Test API")

@app.get("/")
def read_root():
    return {
        "message": "Simple API is working!",
        "vercel": os.getenv("VERCEL", "false"),
        "python_version": os.sys.version
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "api": "simple_test"}