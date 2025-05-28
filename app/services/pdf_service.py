import os
import uuid
import pdfplumber
from fastapi import UploadFile
from datetime import datetime
from app.models.document_model import db

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

async def handle_pdf_upload(file: UploadFile):
    os.makedirs("uploads", exist_ok=True)
    doc_id = str(uuid.uuid4())
    path = f"uploads/{doc_id}_{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    text = extract_text_from_pdf(path)
    doc = {
        "_id": doc_id,
        "filename": file.filename,
        "path": path,
        "text": text,
        "upload_time": datetime.utcnow()
    }
    db.insert_one(doc)
    return {"doc_id": doc_id, "filename": file.filename}

def get_document_by_id(doc_id):
    doc = db.find_one({"_id": doc_id})
    if not doc:
        return {"error": "Document not found"}
    return {
        "doc_id": doc["_id"],
        "filename": doc["filename"],
        "upload_time": doc["upload_time"],
        "text": doc["text"][:1000]
    }

def get_documents_paginated(page: int, limit: int):
    skip = (page - 1) * limit
    docs = list(db.find().skip(skip).limit(limit))
    return [{
        "doc_id": doc["_id"],
        "filename": doc["filename"],
        "upload_time": doc["upload_time"]
    } for doc in docs]
