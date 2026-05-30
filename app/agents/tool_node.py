import re

from app.tools.tool_registry import (
    tool_registry
)

def extract_vehicle_id(query):

    match = re.search(
        r"V\d+",
        query
    )

    if match:

        return match.group()

    return None

def tool_node(state):

    query = state["query"]

    vehicle_id = extract_vehicle_id(query)

    tool_results = {}

    if vehicle_id:

        tool_results[
            "vehicle_info"
        ] = tool_registry[
            "vehicle_lookup"
        ](vehicle_id)

        tool_results[
            "maintenance"
        ] = tool_registry[
            "maintenance_status"
        ](vehicle_id)

        tool_results[
            "alerts"
        ] = tool_registry[
            "gps_alerts"
        ](vehicle_id)

    state["tool_results"] = tool_results

    return state