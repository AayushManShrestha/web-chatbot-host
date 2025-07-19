# app/chain_utils.py
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from app.vectorstore_loader import load_vectorstore
from app.llm_loader import load_llm
from app.prompts import qa_prompt

def create_qa_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    llm = load_llm()
    qa_chain = create_stuff_documents_chain(llm, qa_prompt)
    return create_retrieval_chain(retriever, qa_chain)