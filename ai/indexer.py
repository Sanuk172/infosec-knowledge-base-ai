"""
Индексатор базы знаний.
Читает Markdown-файлы угроз и сохраняет чанки в index.json.
Запуск: python indexer.py
"""

import json
import pathlib
import re

THREATS_DIR = pathlib.Path("../site/docs/threats")
INDEX_FILE = pathlib.Path("index.json")


def parse_md(path: pathlib.Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    # убираем frontmatter
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)

    chunks = []
    current_heading = path.stem
    current_lines = []

    for line in text.splitlines():
        if line.startswith("#"):
            if current_lines:
                body = "\n".join(current_lines).strip()
                if body:
                    chunks.append({
                        "file": path.name,
                        "heading": current_heading,
                        "text": body,
                    })
            current_heading = line.lstrip("#").strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        body = "\n".join(current_lines).strip()
        if body:
            chunks.append({
                "file": path.name,
                "heading": current_heading,
                "text": body,
            })

    return chunks


def build_index():
    if not THREATS_DIR.exists():
        print(f"Папка не найдена: {THREATS_DIR}")
        return

    all_chunks = []
    files = sorted(THREATS_DIR.glob("ubi-*.md"))

    for f in files:
        all_chunks.extend(parse_md(f))

    INDEX_FILE.write_text(
        json.dumps(all_chunks, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"Индекс построен: {len(files)} угроз, {len(all_chunks)} чанков -> {INDEX_FILE}")


if __name__ == "__main__":
    build_index()
