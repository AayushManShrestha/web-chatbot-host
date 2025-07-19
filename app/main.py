# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage

from app.chain_utils import create_qa_chain
from app.intent_router import detect_intent
from app.config import MAX_HISTORY_SIZE

app = FastAPI()
qa_chain = create_qa_chain()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    input: str
    history: list[dict]

class ChatResponse(BaseModel):
    answer: str

@app.get("/")
def read_root():
    return {"status": "ok", "message": "🚀 FastAPI backend is running."}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    print("\n=== Incoming Request ===")
    print(f"User input: {req.input}")

    # Trim and format history
    req.history = req.history[-MAX_HISTORY_SIZE * 2:]
    formatted_history = []
    for msg in req.history:
        if msg["role"] == "user":
            formatted_history.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            formatted_history.append(AIMessage(content=msg["content"]))

    print(f"Formatted Chat History: [{len(formatted_history)} messages]")

    # Early intent match
    intent_response = detect_intent(req.input)
    if intent_response:
        print("Returning early due to matched intent.")
        return {"answer": intent_response}

    # Call chain with input and history
    inputs = {
        "input": req.input,
        "chat_history": formatted_history
    }

    result = qa_chain.invoke(inputs)
    print(f"Response: {result['answer']}")
    print("=========================\n")

    return {"answer": result["answer"]}