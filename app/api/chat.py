from fastapi import APIRouter
from app.services.rag_pipeline import ask_question

router = APIRouter()

@router.post("/chat")
async def chat(question: str):

    answer = ask_question(question)

    return {"answer": answer}