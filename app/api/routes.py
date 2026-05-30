from fastapi import APIRouter

from app.rag.pipeline import ingest_documents
from app.rag.retriever import retrieve_documents
from app.rag.generate_response import (
    generate_rag_response
)
from app.memory.session_manager import (
    clear_session
)

from app.agents.agent_executor import (
    run_agent
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

    session_id = payload.get(
        "session_id",
        "default"
    )

    result = run_agent(
        query=query,
        session_id=session_id
    )

    return {
        "query": result["query"],
        "response": result["response"],
        "session_id": result["session_id"]
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

@router.delete("/session/{session_id}")
def delete_session(session_id: str):

    clear_session(session_id)

    return {
        "status": "Session cleared",
        "session_id": session_id
    }