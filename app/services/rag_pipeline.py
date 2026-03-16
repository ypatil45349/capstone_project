from app.services.vector_store import vector_db
from langchain_community.llms import HuggingFaceHub

llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={"temperature": 0.5, "max_length": 512}
)

def ask_question(question):

    docs = vector_db.similarity_search(question, k=3)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    prompt = f"""
Answer using this context:

{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response