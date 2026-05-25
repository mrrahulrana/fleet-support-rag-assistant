from app.rag.retriever import retrieve_documents

query = "How are overspeed alerts generated?"

results = retrieve_documents(query)

for result in results:

    print("\\n--- RESULT ---")
    print(result.page_content)