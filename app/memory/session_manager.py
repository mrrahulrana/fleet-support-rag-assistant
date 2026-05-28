from app.memory.conversation_memory import (
    conversation_sessions
)

def clear_session(session_id):

    if session_id in conversation_sessions:

        del conversation_sessions[session_id]

def clear_all_sessions():

    conversation_sessions.clear()