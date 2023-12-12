<template>
  <div class="dialog__header">
    <div class="dialog__header-avatar">
      <!--      <img :src="require(`@/static/img/avatars/${ chatInfo[activeChatData.index].avatar }`)" :alt="chatInfo.name">-->
      <img :src="require(`@/static/img/avatars/default.png`)" :alt="chatInfo.name">
    </div>
    <div class="dialog__header-name">
      <h2>
        {{ chatInfo[activeChatData.index].dialog_name }}
      </h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DialogHeaderComponent',
  props: [
    'chatInfo',
    'activeChatData'
  ]
}
</script>

<style scoped lang="scss">
.dialog__header {
  position: sticky;
  backdrop-filter: blur(10px);
  top: 0;
  flex: 0.1;
  display: flex;
  justify-content: space-between;
  padding: 25px 0;
  border-bottom: 1px solid #ccc;
  transform: translate(0, -20px);
  z-index: 1;

  &-avatar {
    margin-left: 3em;
    flex: 0.5;
    display: flex;
    align-items: center;

    & img {
      width: 60px;
      height: 60px;
      border-radius: 50%;
    }
  }
  &-name {
    flex: 3;
    display: flex;
    align-items: center;
  }
}
</style>
