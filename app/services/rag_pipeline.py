import os
from app.services.vector_store import get_vector_db
from langchain_groq import ChatGroq

llm = None

def get_llm():
    global llm

    if llm is None:
        llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.1-8b-instant"
        )

    return llm


def ask_question(question):
    db = get_vector_db()
    docs = db.similarity_search(question, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""Answer using this context.

Context:
{context}

Question:
{question}
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content