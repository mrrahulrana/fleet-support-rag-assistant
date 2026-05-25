from pathlib import Path

def load_documents(data_path="data/sample_support_docs"):

    documents = []

    path = Path(data_path)

    for file in path.glob("*.txt"):

        with open(file, "r", encoding="utf-8") as f:

            text = f.read()

            documents.append({
                "file_name": file.name,
                "content": text
            })

    return documents