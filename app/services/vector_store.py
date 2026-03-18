from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

os.makedirs("data/vector_db", exist_ok=True)

vector_db = None


def get_vector_db():
    global vector_db

    if vector_db is None:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        vector_db = Chroma(
            persist_directory="data/vector_db",
            embedding_function=embeddings
        )

    return vector_db

def store_chunks(chunks):
    db = get_vector_db()
    db.add_texts(texts=chunks)
    db.persist()