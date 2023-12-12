<template>
  <div class="wrapper">
    <ChatsComponent :chats="chats" :active-chat="activeChat" />
    <DialogComponent :chats="chats" :active-chat-data="activeChatData" :web-socket="webSocket" @writeChatMessageEmit="writeChatMessage" />
  </div>
</template>

<script>
import DialogComponent from '~/components/Dialog/DialogComponent'

export default {
  name: 'IndexComponent',
  components: {
    DialogComponent
  },
  data () {
    return {
      webSocket: '',
      chats: [],
      activeChatData: ''
    }
  },
  mounted () {
    this.webSocket = new WebSocket('ws://localhost:8000/ws/chat/')

    this.webSocket.onmessage = (event) => {
      const data = JSON.parse(event.data).data
      for (const i in this.chats) {
        if (data.dialog_id === this.chats[i].dialog_id) {
          const messageInfo = {
            text: data.text,
            time: data.time,
            type: data.type
          }
          this.chats[i].messages.push(messageInfo)
        }
      }
    }
  },
  async created () {
    try {
      const response = await this.$axios.post('http://127.0.0.1:8000/api/get_dialogs/', null, {
        headers: {
          Authorization: `Token ${this.$cookies.get('token')}`
        }
      })
      this.chats.push(response.data)
      this.chats = this.chats[0]
    } catch (error) {
      await this.$router.push('/login')
    }
  },
  methods: {
    activeChat (data) {
      this.activeChatData = data
    },
    writeChatMessage (data) {
      this.chats[data.index].messages.push({
        type: 'out',
        text: data.message,
        time: data.time
      })
    }
  }
}
</script>

<style scoped lang="scss">
.h1 {
  font-size: clamp(var(--fs-h1-text), 3vw, calc(var(--fs-h1-text) * 1.1));
  cursor: default;
}

.wrapper {
  height: 80vh;
  flex: 1 2 0;
  display: flex;
  border-radius: 3em;
  /*background: rgba(93, 69, 43, 0.8);*/
  background: var(--wrapper-bg-color);
  box-shadow: 0 0 5em 1em var(--wrapper-border-color);
  color: #fcfcfc;
  transition: 0.5s ease;
  z-index: 10;
  overflow: hidden;
}

.wrapper input {
  margin-top: 30px;
  background: transparent;
  border: 0;
  border-bottom: 2px solid #444035;
  color: #fcfcfc;
  padding: 5px 8px;
  outline: none;
}

.wrapper:focus {
  border-bottom-color: #6e2d7d;
}

.wrapper button {
  background: var(--wrapper-button-color);
  color: #fcfcfc;
  border-radius: 10px;
  border: 2px solid var(--wrapper-button-border-color);
  padding: calc(var(--fs-text) * 1.2) calc(var(--fs-text) * 1.3);
  margin: 1em;
  cursor: pointer;
}

.wrapper button:disabled {
  background: var(--wrapper-button-disabled-color);
  cursor: not-allowed;
}

input, .wrapper button, .h1, .card-info__clouds, .card-info__now, .card-info__fells-like, .card-info__temp-min, .card-info__temp-max {
  transition: all 0.5s ease;
}

input:hover, .wrapper button:hover, .h1:hover, .card-info__clouds:hover, .card-info__now:hover, .card-info__fells-like:hover, .card-info__temp-min:hover, .card-info__temp-max:hover {
  transform: scale(1.1) translateY(-5px);
  filter: drop-shadow(0 0 20px var(--drop-shadow));
}

.chats-search, .dialog {
  height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
  padding: 2vh 0;
}

.chats-search {
  flex: 1;
  border-right: 1px solid #ccc;
}

.dialog {
  flex: 2;
  position: relative;
}

.error {
  color: rgba(208, 57, 57, 0.84);
}
</style>
