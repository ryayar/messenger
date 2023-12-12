<template>
  <div v-if="activeChatData.index + 1" class="dialog">
    <DialogHeaderComponent :chat-info="chats" :active-chat-data="activeChatData" />
    <DialogBodyComponent :chat-info="chats" :active-chat-data="activeChatData" />
    <DialogFooterComponent ref="footer" :chat-info="chats" :active-chat-data="activeChatData" :web-socket="webSocket" @transferMessageEmit="transferMessage" />
  </div>
  <div v-else class="dialog" />
</template>

<script>
import DialogHeaderComponent from '~/components/Dialog/DialogHeaderComponent'
import DialogBodyComponent from '~/components/Dialog/DialogBodyComponent'
import DialogFooterComponent from '~/components/Dialog/DialogFooterComponent'
export default {
  name: 'DialogComponent',
  components: {
    DialogFooterComponent,
    DialogBodyComponent,
    DialogHeaderComponent
  },
  props: [
    'webSocket',
    'chats',
    'activeChatData'
  ],
  methods: {
    transferMessage (data) {
      this.$emit('writeChatMessageEmit', data)
    }
  }
}
</script>

<style scoped lang="scss">
.dialog {
  display: flex;
  flex-direction: column;
}
</style>
