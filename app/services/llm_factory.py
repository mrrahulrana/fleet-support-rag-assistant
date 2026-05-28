import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_llm():

    provider = os.getenv(
        "LLM_PROVIDER",
        "groq"
    )

    if provider == "openai":

        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2
        )

    elif provider == "groq":

        return ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.2
        )

    elif provider == "gemini":

        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.2
        )

    else:

        raise ValueError(
            f"Unsupported provider: {provider}"
        )