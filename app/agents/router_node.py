def router_node(state):

    query = state["query"]

    query_lower = query.lower()

    if "v" in query_lower:

        return "tools"

    return "retrieve"