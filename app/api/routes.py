from fastapi import APIRouter

from app.rag.pipeline import ingest_documents
from app.rag.retriever import retrieve_documents

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