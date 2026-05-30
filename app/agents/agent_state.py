from typing import TypedDict

class AgentState(TypedDict):

    query: str

    session_id: str

    retrieved_context: str

    tool_results: dict

    response: str