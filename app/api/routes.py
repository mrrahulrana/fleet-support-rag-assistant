from fastapi import APIRouter

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