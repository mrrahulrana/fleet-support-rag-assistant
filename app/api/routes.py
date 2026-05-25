from fastapi import APIRouter
from app.rag.pipeline import ingest_documents

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }

@router.post("/chat")
def chat(query: dict):

    return {
        "query": query,
        "response": "LLM response placeholder"
    }

@router.post("/ingest-documents")
def ingest():

    chunks = ingest_documents()

    return {
        "status": "Documents processed",
        "chunks_created": len(chunks)
    }