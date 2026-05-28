from app.services.llm_factory import (
    get_llm
)

def generate_response(prompt):

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content