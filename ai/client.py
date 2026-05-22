"""
Точка входа AI-модуля. Запускает интерактивный RAG-ассистент.
Использование:
    python client.py
"""

from rag import ask


def main():
    print("=== AI-ассистент базы знаний по ИБ ===")
    print("Задайте вопрос или введите 'выход' для завершения.\n")
    while True:
        question = input("Вопрос: ").strip()
        if not question:
            continue
        if question.lower() in ("выход", "exit", "quit"):
            break
        print(f"\n{ask(question)}\n")


if __name__ == "__main__":
    main()
