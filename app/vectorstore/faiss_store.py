from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from app.embeddings.embedding_service import (
    get_embedding_model
)

def create_vector_store(chunks):

    embedding_model = get_embedding_model()

    documents = []

    for chunk in chunks:

        documents.append(
            Document(
                page_content=chunk["content"],
                metadata={
                    "source": chunk["source"]
                }
            )
        )

    vector_store = FAISS.from_documents(
        documents,
        embedding_model
    )

    vector_store.save_local("faiss_index")

    return vector_store