---
layout: home

hero:
  name: "База знаний по ИБ"
  text: "Веб-портал с AI-ассистентом"
  tagline: "227 угроз ФСТЭК + интеллектуальный помощник на основе RAG — задай вопрос и получи ответ с источником"

features:
  - icon: 🗄️
    title: Базы данных
    details: 227 угроз БДУ ФСТЭК с описанием, источником и объектом воздействия для каждой угрозы
    link: /threats/
    linkText: Открыть базы данных
  - icon: 🤖
    title: AI Ассистент
    details: Задай вопрос по информационной безопасности — ответ формируется строго по материалам базы с указанием источника
    link: /assistant/
    linkText: Спросить ассистента
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
