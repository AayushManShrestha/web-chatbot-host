# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

VECTORSTORE_DIR = "app/faiss_index"
EMBEDDING_MODEL = "models/embedding-001"
LLM_PROVIDER = "Groq"
MAX_HISTORY_SIZE = 2