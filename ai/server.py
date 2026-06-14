"""
FastAPI сервер AI-ассистента.
Запуск: uvicorn server:app --reload --port 8000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag import ask, load_index

app = FastAPI(title="InfoSec AI Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

chunks = load_index()


class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_endpoint(q: Question):
    if not q.question.strip():
        return {"answer": "Введите вопрос."}
    return {"answer": ask(q.question, chunks)}


@app.get("/health")
def health():
    return {"status": "ok", "chunks": len(chunks)}
