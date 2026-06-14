"""
Конвертер БДУ ФСТЭК из Excel в Markdown-страницы для VitePress.
Запуск: python ai/excel_to_md.py
"""

import openpyxl
import pathlib
import re

EXCEL_PATH = pathlib.Path(r"C:\Users\1\Downloads\AyuGram Desktop\thrlist (2).xlsx")
OUT_DIR = pathlib.Path("site/docs/threats")


def clean(text) -> str:
    if text is None:
        return ""
    text = str(text)
    text = text.replace("_x000D_", "").replace("\r", "")
    return text.strip()


def level(val) -> str:
    if val == 1:
        return "Да"
    if val == 0:
        return "Нет"
    return "—"


def slug(num: int) -> str:
    return f"ubi-{num:03d}"


def build_md(row: dict) -> str:
    num = row["id"]
    title = row["name"]

    lines = [
        f"---",
        f'title: "УБИ.{num:03d} — {title}"',
        f"---",
        f"",
        f"# УБИ.{num:03d} — {title}",
        f"",
        f"## Описание",
        f"",
        row["desc"] or "_Описание отсутствует._",
        f"",
        f"## Источник угрозы",
        f"",
        row["source"] or "—",
        f"",
        f"## Объект воздействия",
        f"",
        row["target"] or "—",
        f"",
        f"## Нарушаемые свойства безопасности",
        f"",
        f"| Свойство | Нарушается |",
        f"|----------|-----------|",
        f"| Конфиденциальность | {level(row['conf'])} |",
        f"| Целостность | {level(row['integ'])} |",
        f"| Доступность | {level(row['avail'])} |",
        f"",
    ]

    if row["date_added"]:
        lines += [f"**Добавлена в БДУ:** {str(row['date_added'])[:10]}  "]
    if row["date_changed"]:
        lines += [f"**Последнее изменение:** {str(row['date_changed'])[:10]}  "]

    return "\n".join(lines)


def build_index(rows: list[dict]) -> str:
    lines = [
        "# Банк данных угроз ФСТЭК",
        "",
        "Перечень актуальных угроз безопасности информации из официального",
        "банка данных угроз ФСТЭК России (БДУ).",
        "",
        f"Всего угроз: **{len(rows)}**",
        "",
        "| ID | Наименование | Объект воздействия |",
        "|----|-------------|-------------------|",
    ]
    for r in rows:
        name = r["name"]
        target = (r["target"] or "—")[:60]
        link = f"[УБИ.{r['id']:03d}]({slug(r['id'])})"
        lines.append(f"| {link} | {name} | {target} |")
    return "\n".join(lines)


def main():
    wb = openpyxl.load_workbook(EXCEL_PATH)
    ws = wb.active

    rows = []
    for row in ws.iter_rows(min_row=3, values_only=True):
        if row[0] is None or not isinstance(row[0], int):
            continue
        rows.append({
            "id":           row[0],
            "name":         clean(row[1]),
            "desc":         clean(row[2]),
            "source":       clean(row[3]),
            "target":       clean(row[4]),
            "conf":         row[5],
            "integ":        row[6],
            "avail":        row[7],
            "date_added":   row[8],
            "date_changed": row[9],
        })

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for r in rows:
        path = OUT_DIR / f"{slug(r['id'])}.md"
        path.write_text(build_md(r), encoding="utf-8")

    (OUT_DIR / "index.md").write_text(build_index(rows), encoding="utf-8")

    print(f"Gotovo: {len(rows)} ugroz -> {OUT_DIR}")


if __name__ == "__main__":
    main()
