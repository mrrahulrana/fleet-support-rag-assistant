from pathlib import Path

from app.rag.retriever import retrieve_documents

from app.services.llm_service import (
    generate_response
)

from app.memory.conversation_memory import (
    add_message,
    build_chat_history
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

def generate_rag_response(
    query,
    session_id="default"
):

    results = retrieve_documents(query)

    context = build_context(results)

    history = build_chat_history(session_id)

    prompt_template = load_prompt()

    final_prompt = prompt_template.format(
        history=history,
        context=context,
        question=query
    )

    response = generate_response(final_prompt)

    add_message(
        session_id,
        "user",
        query
    )

    add_message(
        session_id,
        "assistant",
        response
    )

    return {
        "query": query,
        "response": response,
        "session_id": session_id,
        "sources": [
            r.metadata for r in results
        ]
    }