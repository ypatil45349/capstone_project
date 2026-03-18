import os

os.makedirs("data/vector_db", exist_ok=True)

vector_db = None


def get_vector_db():
    global vector_db

    if vector_db is None:
        from langchain_community.vectorstores import Chroma
        from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

        embeddings = HuggingFaceInferenceAPIEmbeddings(
            api_key=os.getenv("HF_API_KEY"),
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