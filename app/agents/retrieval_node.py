from app.rag.retriever import retrieve_documents

def retrieval_node(state):

    query = state["query"]

    results = retrieve_documents(query)

    context = ""

    for result in results:

        context += result.page_content + "\n\n"

    state["retrieved_context"] = context

    return state