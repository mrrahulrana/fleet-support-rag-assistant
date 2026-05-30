from app.agents.agent_workflow import (
    agent_graph
)

def run_agent(
    query,
    session_id="default"
):

    result = agent_graph.invoke({

        "query": query,

        "session_id": session_id,

        "retrieved_context": "",

        "tool_results": {},

        "response": ""
    })

    return result