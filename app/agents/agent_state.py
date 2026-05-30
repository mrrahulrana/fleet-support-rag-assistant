from typing import TypedDict

class AgentState(TypedDict):

    query: str

    session_id: str

    retrieved_context: str

    response: str