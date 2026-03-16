from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Create embedding model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Create vector database
vector_db = Chroma(
    persist_directory="data/vector_db",
    embedding_function=embeddings
)

def store_chunks(chunks):

    vector_db.add_texts(chunks)

    vector_db.persist()