# Fleet Support RAG Assistant

LLM-powered customer support assistant using Retrieval-Augmented Generation (RAG), semantic retrieval, and conversational AI workflows for fleet management operations.

---

## 🚀 Features

- Retrieval-Augmented Generation (RAG)
- Semantic document retrieval
- Fleet support conversational assistant
- OpenAI-powered response generation
- FAISS vector database
- FastAPI backend
- Streamlit chat interface
- Document ingestion pipeline
- Intelligent text chunking
- Semantic document preparation

---

## 🏗️ Architecture

```mermaid
flowchart LR

A[Support Documents] --> B[Embedding Pipeline]
B --> C[FAISS Vector Store]

D[User Query] --> E[Retriever]
E --> C

C --> F[Relevant Context]
F --> G[OpenAI LLM]

G --> H[Generated Response]
```

---

## 🛠️ Tech Stack

- Python
- FastAPI
- LangChain
- LangGraph
- OpenAI APIs
- FAISS
- Streamlit
- Docker

---

## 📦 Setup

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run application

```bash
uvicorn app.main:app --reload
```

---

## 📡 API Endpoints

| Endpoint | Description |
|---|---|
| GET /health | Health check |
| POST /chat | Chat endpoint |

---

## 🔮 Future Enhancements

- Multi-agent support workflows
- PostgreSQL integration
- Conversation memory
- Real-time fleet telemetry integration
- Ticket automation