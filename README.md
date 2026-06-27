# База знаний по информационной безопасности

Веб-портал с 227 угрозами из банка данных угроз ФСТЭК России (БДУ) и встроенным AI-ассистентом на основе архитектуры RAG и Google Gemini 2.5 Flash.

**Сайт:** https://sanuk172.github.io/infosec-knowledge-base-ai/

---

## Что умеет система

- Просмотр всех 227 угроз БДУ ФСТЭК с описанием, объектом воздействия и нарушителем
- AI-ассистент принимает вопрос в свободной форме и отвечает строго по данным базы
- Ответ всегда содержит номера УБИ — источники, которые можно проверить
- Архитектура RAG исключает галлюцинации: модель не придумывает, а опирается на найденные угрозы

## Архитектура

```
Браузер → VitePress (Vue 3) → FastAPI (Python) → RAG → Gemini 2.5 Flash
                                                    ↓
                                              index.json
                                          (227 угроз БДУ ФСТЭК)
```

При запросе к ассистенту:
1. Vue-компонент отправляет POST-запрос на FastAPI (`localhost:8000/ask`)
2. RAG ищет топ-5 релевантных угроз в `index.json`
3. Gemini получает найденные угрозы как контекст и формулирует ответ
4. Ответ с номерами УБИ возвращается в браузер

## Структура проекта

```
web-site_with_ai/
├── ai/
│   ├── server.py          # FastAPI-сервер, эндпоинт /ask
│   ├── rag.py             # поиск по индексу + запрос к Gemini
│   ├── indexer.py         # сборка index.json из Markdown-файлов
│   ├── excel_to_md.py     # конвертация исходного Excel БДУ в Markdown
│   ├── index.json         # индекс 227 угроз (генерируется indexer.py)
│   ├── requirements.txt
│   └── .env               # API-ключ и настройки (не коммитится)
├── site/
│   └── docs/
│       ├── threats/        # 227 файлов ubi-001.md … ubi-227.md
│       ├── assistant/      # страница AI-ассистента
│       └── .vitepress/
│           ├── config.mts  # навигация, сайдбар
│           └── theme/
│               ├── AiChat.vue   # Vue-компонент чата
│               └── custom.css
├── start.bat              # запуск одной командой (авто-установка)
└── setup.bat              # ручная установка зависимостей
```

## Требования

- [Node.js LTS](https://nodejs.org)
- [Python 3.10+](https://python.org)
- API-ключ Google Gemini — бесплатно на [aistudio.google.com](https://aistudio.google.com)

## Установка и запуск

### Быстрый способ

```bat
start.bat
```

При первом запуске автоматически установит все зависимости (`npm install` + `pip install`), затем откроет браузер.

### Ручная установка

```bat
setup.bat
```

Или по шагам:

```bash
# Python-зависимости
cd ai
pip install -r requirements.txt

# Node.js-зависимости
cd site
npm install
```

### Настройка API-ключа

Создать или отредактировать файл `ai/.env`:

```env
GEMINI_API_KEY=ваш_ключ_здесь
GEMINI_MODEL=gemini-2.5-flash
DOCS_PATH=../site/docs
```

### Запуск вручную (два терминала)

```bash
# Терминал 1 — AI-бэкенд (порт 8000)
cd ai
python -m uvicorn server:app --reload

# Терминал 2 — сайт (порт 5173)
cd site
npm run docs:dev:host
```

Открыть в браузере: `http://localhost:5173/infosec-knowledge-base-ai/`

## Переменные окружения

| Переменная | Назначение |
|------------|-----------|
| `GEMINI_API_KEY` | Ключ доступа к Gemini API |
| `GEMINI_MODEL` | Имя модели (по умолчанию `gemini-2.5-flash`) |
| `DOCS_PATH` | Путь к папке с Markdown-угрозами для индексатора |

Файл `ai/.env` добавлен в `.gitignore` и не коммитится в репозиторий.

## Деплой

GitHub Actions (`.github/workflows/`) автоматически собирает VitePress и публикует на GitHub Pages при каждом push в `master`.

AI-бэкенд работает локально — для продакшн-деплоя FastAPI можно вынести на любой Python-хостинг (Railway, Render, VPS).

## Технологический стек

| Слой | Технология |
|------|-----------|
| Фронтенд | VitePress 1.6, Vue 3 |
| Компонент чата | Vue 3 (`AiChat.vue`) |
| Бэкенд | Python, FastAPI, Uvicorn |
| AI | Google Gemini 2.5 Flash (`google-genai` SDK) |
| Поиск | RAG (Retrieval-Augmented Generation) |
| Данные | 227 угроз БДУ ФСТЭК, конвертированы из Excel |
| CI/CD | GitHub Actions → GitHub Pages |

## Команда

| Роль | Участник | Группа |
|------|----------|--------|
| Тимлид | Трунёв Даниил Константинович | РИ-151004 |
| Аналитик | Шпетер Альберт Сергеевич | РИ-151004 |
| Дизайнер | Ковалёв Данила Юрьевич | РИ-151004 |
| Разработчик | Власов Александр Сергеевич | РИ-151004 |
