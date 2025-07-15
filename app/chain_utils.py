from langchain.chains import create_retrieval_chain
from app.vectorstore_loader import load_vectorstore
from app.llm_loader import load_llm
from app.prompts import contextualize_q_prompt, qa_prompt
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_history_aware_retriever

def create_qa_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    llm = load_llm()

    # History-aware retriever, using the external context
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    # Chain for answering questions using documents retrieved by the retriever
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    # Combine both parts into one retrieval chain
    return create_retrieval_chain(history_aware_retriever, question_answer_chain)