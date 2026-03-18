from fastapi import FastAPI
from app.api import documents, chat
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()
app = FastAPI()

app.include_router(documents.router)
app.include_router(chat.router)

@app.get("/")
def home():
    return {"message": "AI Document Assistant API running"}

# Lazy-load heavy routers after app starts
@app.on_event("startup")
async def startup():
    from app.api import documents, chat
    app.include_router(documents.router)
    app.include_router(chat.router)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)