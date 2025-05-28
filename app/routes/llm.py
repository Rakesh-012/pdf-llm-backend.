from fastapi import APIRouter, Depends, HTTPException
from app.services.llm_service import summarize_by_doc_id, answer_question
from app.utils.auth import verify_jwt_token

router = APIRouter()

@router.post("/summarize/{doc_id}")
def summarize(doc_id: str, token: str = Depends(verify_jwt_token)):
    return summarize_by_doc_id(doc_id)

@router.post("/query/{doc_id}/{question}")
def query_doc(doc_id: str, question: str, token: str = Depends(verify_jwt_token)):
    return answer_question(doc_id, question)
