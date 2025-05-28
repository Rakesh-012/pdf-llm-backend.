from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import handle_pdf_upload, get_document_by_id, get_documents_paginated
from typing import Optional

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    return await handle_pdf_upload(file)

@router.get("/{doc_id}")
async def get_document(doc_id: str):
    return get_document_by_id(doc_id)

@router.get("/")
async def list_documents(page: int = 1, limit: int = 10):
    return get_documents_paginated(page, limit)
