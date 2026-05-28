conversation_sessions = {}

def get_conversation_history(session_id):

    if session_id not in conversation_sessions:

        conversation_sessions[session_id] = []

    return conversation_sessions[session_id]

def add_message(session_id, role, content):

    history = get_conversation_history(session_id)

    history.append({
        "role": role,
        "content": content
    })

def build_chat_history(session_id):

    history = get_conversation_history(session_id)

    formatted_history = ""

    for message in history:

        formatted_history += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    return formatted_history