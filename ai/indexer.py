"""
Индексатор Markdown-страниц базы знаний.
Читает .md файлы из site/docs, разбивает по заголовкам на чанки
и сохраняет векторный индекс для RAG-поиска.
"""

import os
import json
import pathlib
from dotenv import load_dotenv

load_dotenv()

DOCS_PATH = pathlib.Path(os.getenv("DOCS_PATH", "../site/docs"))
INDEX_PATH = pathlib.Path("index.json")


def split_by_headings(text: str, source: str) -> list[dict]:
    chunks = []
    current_heading = "Введение"
    current_lines = []

    for line in text.splitlines():
        if line.startswith("#"):
            if current_lines:
                chunks.append({
                    "source": source,
                    "heading": current_heading,
                    "text": "\n".join(current_lines).strip(),
                })
            current_heading = line.lstrip("#").strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        chunks.append({
            "source": source,
            "heading": current_heading,
            "text": "\n".join(current_lines).strip(),
        })

    return [c for c in chunks if c["text"]]


def build_index() -> list[dict]:
    chunks = []
    for md_file in DOCS_PATH.rglob("*.md"):
        if ".vitepress" in md_file.parts:
            continue
        relative = str(md_file.relative_to(DOCS_PATH))
        text = md_file.read_text(encoding="utf-8")
        chunks.extend(split_by_headings(text, relative))

    INDEX_PATH.write_text(json.dumps(chunks, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Индекс построен: {len(chunks)} чанков → {INDEX_PATH}")
    return chunks


if __name__ == "__main__":
    build_index()
