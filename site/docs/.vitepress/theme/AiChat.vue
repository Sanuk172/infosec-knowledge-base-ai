<template>
  <div class="ai-chat">
    <div class="ai-chat__messages" ref="messagesEl">
      <div v-if="messages.length === 0" class="ai-chat__placeholder">
        Задайте вопрос об угрозах информационной безопасности из базы ФСТЭК.
        Например: <em>«Какие угрозы связаны с BIOS?»</em>
      </div>
      <div
        v-for="(msg, i) in messages"
        :key="i"
        :class="['ai-chat__message', `ai-chat__message--${msg.role}`]"
      >
        <span class="ai-chat__label">{{ msg.role === 'user' ? 'Вы' : 'Ассистент' }}</span>
        <div class="ai-chat__text" v-html="formatText(msg.text)" />
      </div>
      <div v-if="loading" class="ai-chat__message ai-chat__message--assistant">
        <span class="ai-chat__label">Ассистент</span>
        <div class="ai-chat__text ai-chat__thinking">Думаю...</div>
      </div>
    </div>

    <div class="ai-chat__input-row">
      <input
        v-model="question"
        class="ai-chat__input"
        type="text"
        placeholder="Введите вопрос..."
        :disabled="loading"
        @keydown.enter="send"
      />
      <button class="ai-chat__btn" :disabled="loading || !question.trim()" @click="send">
        {{ loading ? '...' : 'Спросить' }}
      </button>
    </div>

    <div v-if="error" class="ai-chat__error">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const API_URL = 'http://localhost:8000/ask'

const question = ref('')
const messages = ref([])
const loading = ref(false)
const error = ref('')
const messagesEl = ref(null)

function formatText(text) {
  return text
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/\n/g, '<br>')
}

async function send() {
  const q = question.value.trim()
  if (!q || loading.value) return

  error.value = ''
  messages.value.push({ role: 'user', text: q })
  question.value = ''
  loading.value = true

  await nextTick()
  if (messagesEl.value) {
    messagesEl.value.scrollTop = messagesEl.value.scrollHeight
  }

  try {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: q }),
    })
    if (!res.ok) throw new Error(`Ошибка сервера: ${res.status}`)
    const data = await res.json()
    messages.value.push({ role: 'assistant', text: data.answer })
  } catch (e) {
    error.value = 'Не удалось подключиться к серверу. Убедитесь что запущен: uvicorn server:app --port 8000'
  } finally {
    loading.value = false
    await nextTick()
    if (messagesEl.value) {
      messagesEl.value.scrollTop = messagesEl.value.scrollHeight
    }
  }
}
</script>

<style scoped>
.ai-chat {
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  overflow: hidden;
  margin: 24px 0;
}

.ai-chat__messages {
  min-height: 200px;
  max-height: 420px;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: var(--vp-c-bg-soft);
}

.ai-chat__placeholder {
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
  text-align: center;
  margin: auto;
}

.ai-chat__message {
  max-width: 85%;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.ai-chat__message--user {
  align-self: flex-end;
  align-items: flex-end;
}

.ai-chat__message--assistant {
  align-self: flex-start;
  align-items: flex-start;
}

.ai-chat__label {
  font-size: 0.75rem;
  color: var(--vp-c-text-2);
}

.ai-chat__text {
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 10px 14px;
  font-size: 0.95rem;
  line-height: 1.6;
}

.ai-chat__message--user .ai-chat__text {
  background: var(--vp-c-brand-soft);
  border-color: var(--vp-c-brand-1);
}

.ai-chat__thinking {
  color: var(--vp-c-text-2);
  font-style: italic;
}

.ai-chat__input-row {
  display: flex;
  gap: 8px;
  padding: 12px;
  border-top: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
}

.ai-chat__input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 0.95rem;
  outline: none;
}

.ai-chat__input:focus {
  border-color: var(--vp-c-brand-1);
}

.ai-chat__btn {
  padding: 8px 18px;
  background: var(--vp-c-brand-1);
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.95rem;
  font-weight: 500;
  transition: opacity 0.2s;
}

.ai-chat__btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.ai-chat__error {
  padding: 10px 12px;
  background: #fee2e2;
  color: #b91c1c;
  font-size: 0.85rem;
  border-top: 1px solid #fca5a5;
}
</style>
