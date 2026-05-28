from pathlib import Path

from app.rag.retriever import retrieve_documents
from app.services.llm_service import get_llm
from app.services.llm_service import (
    generate_response
)

def load_prompt():

    prompt_path = Path(
        "app/prompts/support_prompt.txt"
    )

    return prompt_path.read_text()

def build_context(results):

    context = ""

    for result in results:

        context += result.page_content + "\n\n"

    return context

def generate_rag_response(query):

    results = retrieve_documents(query)

    context = build_context(results)

    prompt_template = load_prompt()

    final_prompt = prompt_template.format(
        context=context,
        question=query
    )

    response = generate_response(final_prompt)

    return {
        "query": query,
        "response": response,
        "sources": [
            r.metadata for r in results
        ]
    }