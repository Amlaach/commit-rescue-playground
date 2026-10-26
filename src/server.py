# NexusPay API Gateway
from fastapi import FastAPI

app = FastAPI(title="NexusPay Cloud", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "healthy", "service": "nexuspay"}
