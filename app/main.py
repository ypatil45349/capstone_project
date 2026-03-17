from fastapi import FastAPI
from app.api import documents, chat
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(documents.router)
app.include_router(chat.router)

@app.get("/")
def home():
    return {"message": "AI Document Assistant API running"}