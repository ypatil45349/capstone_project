import os
from app.services.vector_store import vector_db
from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

def ask_question(question):
    docs = vector_db.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    # Note: Chat models prefer a list of messages
    prompt = f"Answer using this context.\n\nContext:\n{context}\n\nQuestion:\n{question}"

    # Use invoke like before
    response = llm.invoke(prompt)

    # Chat models return a message object, so we extract the content
    return response.content