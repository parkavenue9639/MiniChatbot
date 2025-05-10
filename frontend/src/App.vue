<template>
  <div class="chat-container">
    <div class="chat-box">
      <div class="chat-window" ref="chatWindow">
        <div
          v-for="(msg, index) in messages"
          :key="index"
          :class="['message', msg.role]"
        >
          <div class="bubble">{{ msg.content }}</div>
        </div>
        <div v-if="typingMessage" class="message bot">
          <div class="bubble typing">{{ typingMessage }}</div>
        </div>
      </div>
      <div class="input-area">
        <input
          v-model="input"
          @keydown.enter="sendMessage"
          type="text"
          placeholder="请输入问题..."
        />
        <button @click="sendMessage" :disabled="loading || !input.trim()">发送</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, nextTick } from 'vue'
import axios from 'axios'

const input = ref('')
const messages = ref([])
const loading = ref(false)
const typingMessage = ref('')
const chatWindow = ref(null)

const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms))

const typeText = async (text) => {
  typingMessage.value = ''
  for (let i = 0; i < text.length; i++) {
    typingMessage.value += text[i]
    await delay(15)
    await nextTick()
    scrollToBottom()
  }
  messages.value.push({ role: 'bot', content: typingMessage.value })
  typingMessage.value = ''
}

const scrollToBottom = () => {
  if (chatWindow.value) {
    chatWindow.value.scrollTop = chatWindow.value.scrollHeight
  }
}

const sendMessage = async () => {
  const content = input.value.trim()
  if (!content || loading.value) return

  messages.value.push({ role: 'user', content })
  input.value = ''
  loading.value = true

  try {
    const res = await axios.post('http://localhost:8000/api/chat/', {
      prompt: content,
      n_predict: 100
    })
    await typeText(res.data.response)
  } catch (err) {
    messages.value.push({ role: 'bot', content: '出错了，请稍后重试。' })
  } finally {
    loading.value = false
  }
}

watch(messages, async () => {
  await nextTick()
  scrollToBottom()
})
</script>

<style scoped>
.chat-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: #f2f2f2;
}

.chat-box {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 800px;
  height: 90vh;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.chat-window {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.message {
  margin-bottom: 10px;
  display: flex;
}

.message.user {
  justify-content: flex-end;
}

.message.bot {
  justify-content: flex-start;
}

.bubble {
  padding: 12px 18px;
  border-radius: 20px;
  max-width: 70%;
  word-break: break-word;
  white-space: pre-wrap;
  line-height: 1.5;
}

.message.user .bubble {
  background-color: #cfe9ff;
  color: #000;
}

.message.bot .bubble {
  background-color: #e6e6e6;
  color: #000;
}

.input-area {
  display: flex;
  padding: 15px;
  border-top: 1px solid #ccc;
  background-color: #fff;
}

.input-area input {
  flex: 1;
  padding: 12px;
  font-size: 16px;
  border-radius: 20px;
  border: 1px solid #ccc;
  outline: none;
  margin-right: 10px;
}

.input-area button {
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 20px;
  border: none;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.input-area button:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}

.typing {
  font-style: italic;
  color: #888;
}
</style>