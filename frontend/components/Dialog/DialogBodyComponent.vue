<template>
  <div class="dialog__body">
    <div v-for="(message, index) in chatInfo[activeChatData.index].messages" :key="index" class="dialog__body-row">
      <div :class="`message-${message.type}`" :style="{ marginTop: getMarginTop(index, message.type) }">
        <p v-text="message.text" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DialogBodyComponent',
  props: [
    'chatInfo',
    'activeChatData'
  ],
  methods: {
    getMarginTop (index, messageType) {
      if (index === 0) {
        return '2em'
      }

      const prevMessage = this.chatInfo[this.activeChatData.index].messages[index - 1]

      if (prevMessage.type === messageType) {
        return '5px'
      } else {
        return '2em'
      }
    }
  }
}
</script>

<style scoped lang="scss">
.dialog__body {
  flex: 2;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;

  &-row {
    & .message-out, & .message-in {
      margin: 0 0.5em;
    }
    & .message-out p, & .message-in p {
      margin: 2px 5px;
      padding: 0.5em 0.8em;
      white-space: break-spaces;
      max-width: 65%;
      border-radius: 1.1em;
    }

    & .message-out {
      display: flex;
      justify-content: flex-end;
      text-align: right;
      &:not(:last-child) {
        margin-top: 0.2em;
      }
      & p {
        background-color: #2C2C2C;
        filter: drop-shadow(0px 0px 4px #151515);
      }
    }

    & .message-in {
      display: flex;
      justify-content: flex-start;
      text-align: left;
      &:not(:last-child) {
        margin-top: 0.2em;
      }
      & p {
        background-color: #0d2c3a;
        filter: drop-shadow(0px 0px 4px #091b21);
      }
    }
  }
}
</style>
