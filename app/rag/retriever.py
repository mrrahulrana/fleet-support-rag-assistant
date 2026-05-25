from langchain_community.vectorstores import FAISS

from app.embeddings.embedding_service import (
    get_embedding_model
)

def retrieve_documents(query):

    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        "faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    results = retriever.invoke(query)

    return results