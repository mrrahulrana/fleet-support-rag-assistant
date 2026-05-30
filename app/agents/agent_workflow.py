from langgraph.graph import StateGraph

from app.agents.agent_state import (
    AgentState
)

from app.agents.router_node import (
    router_node
)

from app.agents.retrieval_node import (
    retrieval_node
)

from app.agents.response_node import (
    response_node
)

from app.agents.tool_node import (
    tool_node
)

workflow = StateGraph(AgentState)

workflow.add_node(
    "retrieve",
    retrieval_node
)

workflow.add_node(
    "respond",
    response_node
)

workflow.add_node(
    "tools",
    tool_node
)

workflow.set_conditional_entry_point(
    router_node,
    {
        "tools": "tools",
        "retrieve": "retrieve"
    }
)

workflow.add_edge(
    "tools",
    "retrieve"
)

workflow.add_edge(
    "retrieve",
    "respond"
)

workflow.set_finish_point(
    "respond"
)

agent_graph = workflow.compile()