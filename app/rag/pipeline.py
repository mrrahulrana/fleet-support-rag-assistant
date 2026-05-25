from app.rag.document_loader import load_documents
from app.rag.text_chunker import chunk_documents

from app.vectorstore.faiss_store import (
    create_vector_store
)

def ingest_documents():

    documents = load_documents()

    chunks = chunk_documents(documents)

    vector_store = create_vector_store(chunks)

    print(f"Loaded {len(documents)} documents")
    print(f"Generated {len(chunks)} chunks")
    print("FAISS vector index created")

    return {
        "documents": len(documents),
        "chunks": len(chunks)
    }

if __name__ == "__main__":

    ingest_documents()