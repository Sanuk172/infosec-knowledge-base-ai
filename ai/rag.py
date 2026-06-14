"""
RAG-модуль: поиск по базе угроз + генерация ответа через Gemini.
"""

import json
import os
import pathlib
import re
from google import genai
from dotenv import load_dotenv

load_dotenv()

INDEX_FILE = pathlib.Path("index.json")
TOP_K = 5

_client = None

def get_client():
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return _client


def load_index() -> list[dict]:
    if not INDEX_FILE.exists():
        raise FileNotFoundError(
            "index.json не найден. Сначала запустите: python indexer.py"
        )
    return json.loads(INDEX_FILE.read_text(encoding="utf-8"))


def search(query: str, chunks: list[dict], top_k: int = TOP_K) -> list[dict]:
    query_words = set(re.findall(r"\w+", query.lower()))
    scored = []
    for chunk in chunks:
        text_words = set(re.findall(r"\w+", chunk["text"].lower()))
        score = len(query_words & text_words)
        if score > 0:
            scored.append((score, chunk))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in scored[:top_k]]


def ask(question: str, chunks: list[dict] | None = None) -> str:
    if chunks is None:
        chunks = load_index()

    relevant = search(question, chunks)

    if not relevant:
        return (
            "В базе знаний не найдено материалов по данному вопросу. "
            "Попробуйте переформулировать запрос."
        )

    context = "\n\n---\n\n".join(
        f"[{c['file']} / {c['heading']}]\n{c['text']}"
        for c in relevant
    )

    prompt = f"""Ты — AI-ассистент базы знаний по информационной безопасности.
Отвечай строго на основе предоставленного контекста из банка угроз ФСТЭК.
Если ответа в контексте нет — честно скажи об этом.
Отвечай на русском языке, кратко и по существу.

Контекст:
{context}

Вопрос пользователя: {question}

Ответ:"""

    model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
    response = get_client().models.generate_content(model=model, contents=prompt)

    sources = list(dict.fromkeys(c["file"].replace(".md", "").upper() for c in relevant))
    sources_text = ", ".join(sources)

    return f"{response.text.strip()}\n\n**Источники:** {sources_text}"
