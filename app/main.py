from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Fleet Support RAG Assistant",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "Fleet Support RAG Assistant"
    }