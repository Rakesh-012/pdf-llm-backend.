from app.models.document_model import db
from app.utils.llm import ask_gemini

def summarize_by_doc_id(doc_id: str):
    doc = db.find_one({"_id": doc_id})
    if not doc:
        return {"error": "Document not found"}
    prompt = "Summarize this text in 2 sentences: " + doc["text"][:3000]
    return {"summary": ask_gemini(prompt)}

def answer_question(doc_id: str, question: str):
    doc = db.find_one({"_id": doc_id})
    if not doc:
        return {"error": "Document not found"}
    
    prompt = (
        f"Answer this question based on the document:\n\n"
        f"Question: {question}\n\n"
        f"Document:\n{doc['text'][:3000]}"
    )
    
    return {"answer": ask_gemini(prompt)}
