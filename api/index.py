from fastapi import FastAPI
import os

# Initialize app
app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello from Vercel!",
        "status": "working",
        "vercel": os.getenv("VERCEL", "false")
    }

@app.get("/api/health")
async def health():
    return {"status": "healthy"}
