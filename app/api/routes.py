from fastapi import APIRouter

from app.rag.pipeline import ingest_documents
from app.rag.retriever import retrieve_documents
from app.rag.generate_response import (
    generate_rag_response
)

router = APIRouter()

@router.get("/health")
def health():

    return {
        "status": "healthy"
    }

@router.post("/chat")
def chat(payload: dict):

    query = payload.get("query")

    result = generate_rag_response(query)

    return result

@router.post("/ingest-documents")
def ingest():

    result = ingest_documents()

    return {
        "status": "Documents processed",
        "details": result
    }

@router.post("/search")
def search(payload: dict):

    query = payload.get("query")

    results = retrieve_documents(query)

    response = []

    for result in results:

        response.append({
            "content": result.page_content,
            "source": result.metadata
        })

    return {
        "query": query,
        "results": response
    }