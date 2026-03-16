from langchain_ollama import OllamaLLM
from app.services.vector_store import vector_db

llm = OllamaLLM(model="llama3")

def ask_question(question):

    docs = vector_db.similarity_search(question, k=3)

    context = ""

    for doc in docs:
        context += doc.page_content

    prompt = f"""
    Answer using this context:

    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response