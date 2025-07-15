from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage
from app.chain_utils import create_qa_chain
from app.intent_router import detect_intent
from app.config import MAX_HISTORY_SIZE

app = FastAPI()
qa_chain = create_qa_chain()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend to access backend
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

    req.history = req.history[:-1][-MAX_HISTORY_SIZE*2:]
    formatted_history = []
    for msg in req.history:
        if msg["role"] == "user":
            formatted_history.append(HumanMessage(content=msg["content"]))
        else:
            formatted_history.append(AIMessage(content=msg["content"]))

    print("Formatted Chat history:", formatted_history)

    # Intent detection
    intent_response = detect_intent(req.input)
    if intent_response:
        print("Returning early due to matched intent.")
        return {"answer": intent_response}

    # Call LangChain RAG chain with user input and chat history
    result = qa_chain.invoke({
        "input": req.input,
        "chat_history": formatted_history
    })

    print(f"Response: {result['answer']}")
    print("=========================\n")

    return {"answer": result["answer"]}