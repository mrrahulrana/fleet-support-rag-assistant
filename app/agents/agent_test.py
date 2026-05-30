from app.agents.agent_executor import (
    run_agent
)

response = run_agent(

    query=(
        "How are overspeed alerts generated?"
    ),

    session_id="fleet-agent-session"
)

print("\n--- AGENT RESPONSE ---\n")

print(response["response"])