"""
Консольный клиент AI-ассистента базы знаний по ИБ.
Запуск: python client.py
"""

from rag import ask, load_index


def main():
    print("=== AI-ассистент базы угроз ФСТЭК ===")
    print("Задайте вопрос об угрозах ИБ или введите 'выход'.\n")

    chunks = load_index()
    print(f"База загружена: {len(chunks)} фрагментов.\n")

    while True:
        question = input("Вопрос: ").strip()
        if not question:
            continue
        if question.lower() in ("выход", "exit", "quit", "q"):
            break
        print()
        print(ask(question, chunks))
        print()


if __name__ == "__main__":
    main()
