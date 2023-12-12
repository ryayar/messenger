<template>
  <div class="dialog__footer">
    <div class="dialog__footer-attach" />
    <div
      ref="messageInput"
      class="dialog__footer-input"
      contenteditable="true"
      @input="change"
      @keydown.enter.exact.shift.prevent="handleShiftEnterKey"
      @keydown.enter.exact="handleEnterKey"
    />
    <div class="dialog__footer-send" @click="send" />
  </div>
</template>

<script>
export default {
  name: 'DialogFooterComponent',
  props: [
    'webSocket',
    'chatInfo',
    'activeChatData'
  ],
  data () {
    return {
      newWebSocket: '',
      newMessage: ''
    }
  },
  mounted () {
    this.$refs.messageInput.focus()
    this.newWebSocket = this.webSocket
  },
  methods: {
    async send () {
      const mess = this.newMessage.split('\n')
      this.newMessage = ''
      for (const i in mess) {
        this.newMessage += `${mess[i].trim()}\n`
      }
      this.newMessage = this.newMessage.trim()
      if (this.newMessage !== '') {
        const activeChatInfo = this.chatInfo[this.activeChatData.index]
        const messageInfo = {
          index: this.activeChatData.index,
          dialog_id: activeChatInfo.dialog_id,
          dialog_name: activeChatInfo.dialog_name,
          message: this.newMessage
        }
        try {
          await this.newWebSocket.send(JSON.stringify(messageInfo))
          this.$emit('transferMessageEmit', messageInfo)
        } catch (error) {
          await this.$router.push('/login')
        }
      }
      this.newMessage = ''
      this.$refs.messageInput.innerHTML = ''
      this.$nextTick(() => {
        this.$refs.messageInput.focus()
      })
    },
    change (e) {
      this.newMessage = e.target.innerText
      console.log(this.newMessage)
    },
    handleShiftEnterKey (event) {
      if (event.shiftKey && event.key === 'Enter') {
        document.execCommand('insertLineBreak')
      }
    },
    handleEnterKey (event) {
      if (!event.shiftKey && event.key === 'Enter') {
        event.preventDefault()
        this.send()
      }
    }
  }
}
</script>

<style scoped lang="scss">
.dialog__footer {
  position: sticky;
  bottom: 0;
  backdrop-filter: blur(10px);
  flex: 0.1;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  border-top: 1px solid #ccc;
  margin-top: 0.5em;
  padding: 1.2em 0;
  transform: translate(0, 1.2em);
  &-attach, &-input, &-send {
    margin: 0 0.3em;
    border-radius: 1em;
    transition: 0.1s ease all;
  }
  &-attach {
    width: 50px;
    height: 50px;
  }
  &-input {
    max-height: 15em;
    min-height: 50px;
    overflow: auto;
    width: 80%;
    outline: none;
    padding: 1em 0.7em;
    background-color: #2d2d2d;
    filter: drop-shadow(0px 0px 10px black);
    &:hover {
      scale: 101%;
    }
  }
  &-send {
    width: 50px;
    height: 50px;
    background-image: url("@/static/img/icon/send.svg");
    background-repeat: no-repeat;
    background-size: 2.5em;
    background-position: center;
    cursor: pointer;
    filter: drop-shadow(0px 0px 10px black);

    &:hover {
      scale: 120%;
      rotate: -90deg;
    }
    &:active {
      transform: translateX(5px);
    }
  }
}
</style>
