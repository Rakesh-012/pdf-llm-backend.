from fastapi import FastAPI
from app.routes import pdf, llm
from app.utils.auth import auth_router

app = FastAPI()

app.include_router(auth_router, tags=["Auth"])
app.include_router(pdf.router, prefix="/documents", tags=["PDF Processing"])
app.include_router(llm.router, prefix="/llm", tags=["LLM Operations"])

@app.get("/")
def root():
    return {"message": "PDF LLM Backend is running."}
