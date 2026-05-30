def router_node(state):

    query = state["query"]

    query_lower = query.lower()

    if (
        "vehicle" in query_lower
        or "alert" in query_lower
        or "gps" in query_lower
        or "maintenance" in query_lower
    ):

        return "retrieve"

    return "respond"