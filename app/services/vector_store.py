import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Ensure vector DB folder exists
os.makedirs("data/vector_db", exist_ok=True)

# Load embedding model once
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector database
vector_db = Chroma(
    persist_directory="data/vector_db",
    embedding_function=embeddings
)


def get_vector_db():
    return vector_db


def store_chunks(chunks):
    db = get_vector_db()

    db.add_texts(texts=chunks)

    db.persist()

    return {"message": "Chunks stored successfully"}