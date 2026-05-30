from pathlib import Path

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

def response_node(state):

    query = state["query"]

    session_id = state["session_id"]

    context = state["retrieved_context"]

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

    state["response"] = response

    return state