from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

os.makedirs("data/vector_db", exist_ok=True)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="data/vector_db",
    embedding_function=embeddings
)

def store_chunks(chunks):
    vector_db.add_texts(chunks)
    vector_db.persist()