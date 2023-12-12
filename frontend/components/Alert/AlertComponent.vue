<template>
  <div class="alert">
    <h1>
      This ALERT!!
    </h1>
  </div>
</template>

<script>
export default {
  name: 'AlertComponent',
  props: {
    msg: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>
.alert {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  margin: 1em auto;
  border: 1px solid snow;
  border-radius: 15px;
  width: 550px;
}
</style>
