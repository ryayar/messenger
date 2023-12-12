<template>
  <div>
    <input type="text" id="messageInput">
    <button onclick="sendMessage()">
      Отправить
    </button>
    <ul id="chatMessages" />
  </div>
</template>

<script>
export default {
  name: 'test',
  mounted() {
    const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/'); // Подставьте адрес вашего сервера

    chatSocket.onopen = function (e) {
      console.log('WebSocket соединение установлено');
    };

    chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      const message = data.message;

      const chatMessages = document.getElementById('chatMessages');
      const messageElement = document.createElement('li');
      messageElement.innerHTML = message;

      chatMessages.appendChild(messageElement);
    };

    function sendMessage() {
      const messageInput = document.getElementById('messageInput');
      const message = messageInput.value;

      chatSocket.send(JSON.stringify({
        'message': message
      }));

      messageInput.value = '';
    }
  }
}
</script>

<style scoped>

</style>
