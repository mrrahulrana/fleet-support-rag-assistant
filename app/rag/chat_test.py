from app.rag.generate_response import (
    generate_rag_response
)

query = "How are overspeed alerts generated?"

response = generate_rag_response(query)

print("\n--- RESPONSE ---\n")

print(response["response"])