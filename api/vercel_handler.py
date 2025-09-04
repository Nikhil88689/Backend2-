from fastapi import FastAPI
from mangum import Mangum
import os

# Create FastAPI app
app = FastAPI(title="Notes API", description="A simple notes app")

@app.get("/")
def read_root():
    return {
        "message": "Notes API is working on Vercel!",
        "status": "healthy",
        "vercel": os.getenv("VERCEL", "false")
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "api": "working"}

# Create ASGI handler for Vercel
handler = Mangum(app)