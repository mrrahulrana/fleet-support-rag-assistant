from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50
    )

    chunks = []

    for doc in documents:

        split_texts = splitter.split_text(doc["content"])

        for chunk in split_texts:

            chunks.append({
                "source": doc["file_name"],
                "content": chunk
            })

    return chunks