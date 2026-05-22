"""
RAG-поиск по индексу базы знаний с использованием Gemini.
Принимает вопрос, находит релевантные чанки и генерирует ответ.
"""

import json
import os
import pathlib
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
INDEX_PATH = pathlib.Path("index.json")
TOP_K = 5


def load_index() -> list[dict]:
    if not INDEX_PATH.exists():
        raise FileNotFoundError("Индекс не найден. Сначала запустите indexer.py")
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def simple_search(query: str, chunks: list[dict], top_k: int = TOP_K) -> list[dict]:
    query_words = set(query.lower().split())
    scored = []
    for chunk in chunks:
        text_words = set(chunk["text"].lower().split())
        score = len(query_words & text_words)
        if score > 0:
            scored.append((score, chunk))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in scored[:top_k]]


def ask(question: str) -> str:
    chunks = load_index()
    relevant = simple_search(question, chunks)

    if not relevant:
        return "В базе знаний не найдено материалов по данному вопросу."

    context = "\n\n---\n\n".join(
        f"[{c['source']} / {c['heading']}]\n{c['text']}" for c in relevant
    )

    prompt = (
        "Ты — ассистент базы знаний по информационной безопасности. "
        "Отвечай только на основе предоставленного контекста. "
        "Если ответа в контексте нет — так и скажи.\n\n"
        f"Контекст:\n{context}\n\n"
        f"Вопрос: {question}\n\nОтвет:"
    )

    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)

    sources = list({f"{c['source']} ({c['heading']})" for c in relevant})
    sources_text = "\n".join(f"• {s}" for s in sources)

    return f"{response.text}\n\n**Источники:**\n{sources_text}"


if __name__ == "__main__":
    while True:
        q = input("\nВопрос (или 'выход'): ").strip()
        if q.lower() in ("выход", "exit", "quit"):
            break
        print(ask(q))
