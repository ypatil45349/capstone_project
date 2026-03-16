from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create vector database
vector_db = Chroma(
    persist_directory="data/vector_db",
    embedding_function=embeddings
)

def store_chunks(chunks):

    vector_db.add_texts(chunks)

    vector_db.persist()