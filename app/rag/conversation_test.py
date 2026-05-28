from app.rag.generate_response import (
    generate_rag_response
)

session_id = "fleet-session-1"

query_1 = (
    "How are overspeed alerts generated?"
)

response_1 = generate_rag_response(
    query=query_1,
    session_id=session_id
)

print("\n--- RESPONSE 1 ---\n")

print(response_1["response"])

query_2 = (
    "What happens after that?"
)

response_2 = generate_rag_response(
    query=query_2,
    session_id=session_id
)

print("\n--- RESPONSE 2 ---\n")

print(response_2["response"])