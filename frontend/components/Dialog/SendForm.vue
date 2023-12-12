<template>
  <div class="dialog__footer-input" contenteditable="true" @input="chanage" />
</template>

<script>
export default {
  name: 'SendForm',
  methods: {
    chanage (e) {
      this.$emit('message-div', e.target.innerText)
    }
  }
}
</script>

<style scoped lang="scss">
.dialog__footer {
  flex: 0.1;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  border-top: 1px solid #ccc;
  margin-top: 0.5em;
  padding: 0.5em 0 0;
  &-attach, &-input, &-send {
    border: 1px solid #ccc;
    margin: 0 0.3em;
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
  }
  &-send {
    width: 50px;
    height: 50px;
  }
}
</style>
