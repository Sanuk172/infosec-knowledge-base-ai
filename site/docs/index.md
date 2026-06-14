---
layout: home

hero:
  name: "База знаний по ИБ"
  text: "Веб-портал с AI-ассистентом"
  tagline: "227 угроз ФСТЭК + интеллектуальный помощник на основе RAG — задай вопрос и получи ответ с источником"
  actions:
    - theme: brand
      text: Угрозы БДУ ФСТЭК
      link: /threats/
    - theme: alt
      text: AI-ассистент
      link: /assistant/
---

<div class="kb-stats">
  <div class="kb-stat">
    <span class="kb-stat-num">227</span>
    <span class="kb-stat-label">угроз из БДУ ФСТЭК</span>
  </div>
  <div class="kb-stat">
    <span class="kb-stat-num">RAG</span>
    <span class="kb-stat-label">архитектура ассистента</span>
  </div>
  <div class="kb-stat">
    <span class="kb-stat-num">Gemini</span>
    <span class="kb-stat-label">языковая модель</span>
  </div>
</div>

## Из чего состоит проект

<div class="kb-cards">
  <div class="kb-card">
    <span class="kb-card-icon">🗄️</span>
    <h3>База угроз ФСТЭК</h3>
    <p class="kb-muted">227 актуальных угроз из официального банка данных угроз ФСТЭК России. Каждая угроза — отдельная страница с описанием, источником и объектом воздействия.</p>
  </div>
  <div class="kb-card">
    <span class="kb-card-icon">🤖</span>
    <h3>AI-ассистент</h3>
    <p class="kb-muted">Отвечает на вопросы только по материалам базы. Исключает галлюцинации и всегда указывает источник — конкретный номер УБИ.</p>
  </div>
  <div class="kb-card">
    <span class="kb-card-icon">🔍</span>
    <h3>Полнотекстовый поиск</h3>
    <p class="kb-muted">Встроенный поиск по всем страницам базы знаний. Найдите нужную угрозу по названию, описанию или объекту воздействия.</p>
  </div>
</div>

## Как работает система

<div class="kb-steps">
  <div class="kb-step">
    <div class="kb-step-num">1</div>
    <div class="kb-step-text">Пользователь задаёт вопрос об угрозе ИБ в произвольной форме</div>
  </div>
  <div class="kb-step">
    <div class="kb-step-num">2</div>
    <div class="kb-step-text">Система ищет релевантные угрозы в базе из 227 записей БДУ ФСТЭК</div>
  </div>
  <div class="kb-step">
    <div class="kb-step-num">3</div>
    <div class="kb-step-text">Gemini 2.5 Flash формирует ответ строго по найденным данным</div>
  </div>
  <div class="kb-step">
    <div class="kb-step-num">4</div>
    <div class="kb-step-text">Ответ возвращается с указанием номеров УБИ — источников информации</div>
  </div>
</div>

## Технологический стек

| Компонент | Технология |
|-----------|-----------|
| Сайт и контент | VitePress (Vue + Markdown) |
| База угроз | БДУ ФСТЭК, 227 угроз |
| AI-ассистент | Google Gemini 2.5 Flash + RAG |
| Бэкенд ассистента | Python FastAPI |
| Деплой | GitHub Actions + GitHub Pages |
