# app/llm_loader.py
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GOOGLE_API_KEY, LLM_PROVIDER
from langchain_groq import ChatGroq

llm = None  # Global variable to cache the LLM instance

def load_llm():
    global llm
    if llm is None:
        if LLM_PROVIDER == "Google":
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                google_api_key=GOOGLE_API_KEY,
                temperature=0.3
            )
        elif LLM_PROVIDER == "Groq":
            llm = ChatGroq(
                model="llama-3.1-8b-instant",
                temperature=0.3
            )
        else:
            raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
    return llm