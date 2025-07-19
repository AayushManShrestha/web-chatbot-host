# app/llm_loader.py
from langchain_groq import ChatGroq

_llm_cache = None

def load_llm():
    """
    Load and return a cached Groq LLM instance (LLaMA 3.1) with fixed settings.
    """
    global _llm_cache
    if _llm_cache is None:
        _llm_cache = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.2,
            max_tokens=256
        )
    return _llm_cache