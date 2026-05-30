from app.agents.agent_executor import (
    run_agent
)

response = run_agent(

    query=(
        "Show maintenance status and alerts for V102"
    ),

    session_id="fleet-tools-session"
)

print("\n--- AGENT RESPONSE ---\n")

print(response["response"])