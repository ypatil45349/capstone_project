from fastapi import APIRouter, UploadFile
import shutil
import os

from app.services.document_processor import process_document
from app.services.vector_store import store_chunks

router = APIRouter()

UPLOAD_PATH = "data/uploads/"


@router.post("/documents")
async def upload_document(file: UploadFile):

    file_path = os.path.join(UPLOAD_PATH, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process document
    chunks = process_document(file_path)

    # Store in vector database
    store_chunks(chunks)

    return {"message": "Document processed and stored successfully"}