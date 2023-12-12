<template>
  <div class="chats-search">
    <div class="search">
      <AutoComplete
        v-model="searchingUsers"
        optionLabel="name"
        :suggestions="usernames"
        @focusout="completeSearchUser"
        @input="searchUser"
      />
    </div>
    <div class="chats">
      <div v-for="(chat, index) in chats" :key="index" class="chat" @click="active(index)">
        <div class="chat__avatar">
          <img :src="require(`@/static/img/avatars/default.png`)" :alt="chat.name">
        </div>
        <div class="chat__message">
          <div class="chat__message-name">
            {{ chat.dialog_name }}
          </div>
          <div class="chat__message-text">
            {{ truncateText(chat.messages[chat.messages.length - 1].text) }}
          </div>
          <div class="chat__message-date">
            {{ chat.messages[chat.messages.length - 1].time }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AutoComplete from 'primevue/AutoComplete'

export default {
  name: 'ChatsComponent',
  props: [
    'chats',
    'activeChat'
  ],
  components: {
    AutoComplete
  },
  data () {
    return {
      searchingUsers: '',
      searchUsers: '',
      usernames: []
    }
  },
  methods: {
    truncateText (text) {
      const maxLength = 25
      if (text.length > maxLength) {
        return `${text.replaceAll('<br>', ' ').slice(0, maxLength)}...`
      }
      return text
    },
    active (index) {
      this.activeChat({
        index
      })
      const allChat = document.querySelectorAll('.chat')
      const needChat = allChat[index]

      for (let i = 0; i < allChat.length; i++) {
        allChat[i].classList.remove('is-active')
      }
      needChat.classList.add('is-active')
    },
    async searchUser () {
      if (!this.searchingUsers) {
        return
      }
      try {
        const data = { username: this.searchingUsers }
        const headers = { headers: { Authorization: `Token ${this.$cookies.get('token')}` } }
        const response = await this.$axios.post('http://127.0.0.1:8000/api/search/', data, headers)
        this.usernames = []
        for (const i in response.data.users) {
          this.usernames.push(response.data.users[i].name)
        }
      } catch (error) {
        console.error('Ошибка при поиске пользователей:', error)
      }
    },
    completeSearchUser (e) {
      console.log(this.searchingUsers)
    }
  }
  // mounted () {
  //   for (const item in this.items) {
  //     this.items[item].avatar = require('@/static/img/avatars/' + this.items[item].avatar)
  //   }
  // },
}
</script>

<style scoped lang="scss">
$gray-name-date: #d0d0d0;
.chats-search {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.chats {
  width: 100%;
}

.chat {
  display: flex;
  border-bottom: 1px solid #333;
  justify-content: space-between;
  align-items: center;
  padding: 0.5em 0.8em;
  cursor: pointer;
  transition: 0.4s;

  &:hover {
    background-color: rgba(87, 42, 134, 0.2);
    scale: 103%
  }

  &.is-active {
    background-color: rgba(87, 42, 134, 0.5);
  }

  &__avatar {
    display: flex;

    & img {
      width: 60px;
      height: 60px;
      border-radius: 50%;
    }
  }

  &__message {
    display: flex;
    flex-direction: column;
    align-items: flex-end;

    &-name {
      font-size: 1em;
      color: $gray-name-date;
    }

    &-text {
      font-size: 1em;
    }

    &-date {
      font-size: 0.8em;
      color: $gray-name-date;
    }
  }
}
</style>
