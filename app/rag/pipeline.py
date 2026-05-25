from app.rag.document_loader import load_documents
from app.rag.text_chunker import chunk_documents

def ingest_documents():

    documents = load_documents()

    chunks = chunk_documents(documents)

    print(f"Loaded {len(documents)} documents")
    print(f"Generated {len(chunks)} chunks")

    return chunks


if __name__ == "__main__":

    ingest_documents()