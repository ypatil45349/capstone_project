from fastapi import FastAPI
from app.api import documents, chat

app = FastAPI()

app.include_router(documents.router)
app.include_router(chat.router)