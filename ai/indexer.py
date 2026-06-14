"""
Индексатор базы знаний.
Каждая угроза → один чанк со всеми полями: название, описание, источник, объект.
Запуск: python indexer.py
"""

import json
import pathlib
import re

THREATS_DIR = pathlib.Path("../site/docs/threats")
INDEX_FILE = pathlib.Path("index.json")


def parse_threat(path: pathlib.Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)

    fields = {}
    current_heading = None
    current_lines = []

    for line in text.splitlines():
        if line.startswith("#"):
            if current_heading:
                fields[current_heading] = "\n".join(current_lines).strip()
            current_heading = line.lstrip("#").strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_heading:
        fields[current_heading] = "\n".join(current_lines).strip()

    title = next((k for k in fields.keys() if "УБИ" in k), "")
    description = fields.get("Описание", "")
    source = fields.get("Источник угрозы", "")
    target = fields.get("Объект воздействия", "")
    props = fields.get("Нарушаемые свойства безопасности", "")

    if not title:
        return None

    full_text = f"{title}\n\nОписание: {description}\n\nИсточник угрозы: {source}\n\nОбъект воздействия: {target}\n\nНарушаемые свойства: {props}"

    return {
        "file": path.name,
        "heading": title,
        "text": full_text,
    }


def build_index():
    if not THREATS_DIR.exists():
        print(f"Папка не найдена: {THREATS_DIR}")
        return

    chunks = []
    files = sorted(THREATS_DIR.glob("ubi-*.md"))

    for f in files:
        chunk = parse_threat(f)
        if chunk:
            chunks.append(chunk)

    INDEX_FILE.write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"Индекс построен: {len(chunks)} угроз -> {INDEX_FILE}")


if __name__ == "__main__":
    build_index()
