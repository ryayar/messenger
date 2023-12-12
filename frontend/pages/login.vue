<template>
  <div class="section">
    <Message v-for="msg of messages" :key="msg" :severity="msg.severity" :sticky="msg.sticky" :life="msg.life">
      {{ msg.content }}
    </Message>
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center py-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
            <h6 class="mb-0 pb-3">
              <span>
                Войти
              </span>
              <span>
                Регистрация
              </span>
            </h6>
            <input id="reg-log" class="checkbox" type="checkbox" name="reg-log">
            <label for="reg-log" />
            <div class="card-3d-wrap mx-auto">
              <div class="card-3d-wrapper">
                <div class="card-front">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 class="mb-4 pb-3">
                        Вход
                      </h4>
                      <div class="form-group">
                        <input
                          id="username"
                          v-model="username"
                          type="text"
                          name="username"
                          class="form-style"
                          placeholder="Имя пользователя"
                          autocomplete="off"
                        >
                        <i class="input-icon uil uil-at" />
                      </div>
                      <div class="form-group mt-2">
                        <input
                          id="password"
                          v-model="password"
                          type="password"
                          name="password"
                          class="form-style"
                          placeholder="Пароль"
                          autocomplete="off"
                        >
                        <i class="input-icon uil uil-lock-alt" />
                      </div>
                      <button class="btn mt-4" @click="login">
                        Войти
                      </button>
                      <button class="btn mt-4" @click="logout">
                        Выйти
                      </button>
                      <button class="btn mt-4" @click="tokens">
                        Токен
                      </button>
                      <p class="mb-0 mt-4 text-center">
                        <a href="#0" class="link">
                          Восстановить пароль
                        </a>
                      </p>
                    </div>
                  </div>
                </div>
                <div class="card-back">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 class="mb-4 pb-3">
                        Регистрация
                      </h4>
                      <div class="form-group">
                        <input
                          id="username"
                          v-model="username"
                          type="text"
                          name="username"
                          class="form-style"
                          placeholder="Имя пользователя"
                          autocomplete="off"
                        >
                        <i class="input-icon uil uil-user" />
                      </div>
                      <div class="form-group mt-2">
                        <input
                          id="password"
                          v-model="password"
                          type="password"
                          name="password"
                          class="form-style"
                          placeholder="Пароль"
                          autocomplete="off"
                        >
                        <i class="input-icon uil uil-lock-alt" />
                      </div>
                      <button class="btn mt-4" @click="register">
                        Зарегистрироваться
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Message from 'primevue/message'
export default {
  name: 'LogIn',
  components: {
    Message
  },
  data () {
    return {
      messages: [],
      username: '',
      password: '',
      token: ''
    }
  },
  methods: {
    async register () {
      try {
        const response = await this.$axios.post('http://127.0.0.1:8000/api/register/', {
          username: this.username,
          password: this.password
        })
        this.messages = [{ severity: response.data.type, content: response.data.message, sticky: false, life: 3000 }]
      } catch (error) {
        this.messages = [{ severity: 'error', content: error, sticky: false, life: 3000 }]
      }
    },
    async login () {
      try {
        const response = await this.$axios.post('http://127.0.0.1:8000/api/login/', {
          username: this.username,
          password: this.password
        })
        this.token = response.data.token
        localStorage.setItem('token', this.token)
        localStorage.setItem('username', this.username)
        this.$cookies.set('token', this.token, { path: '/' })
        this.messages = [{ severity: response.data.type, content: `${response.data.message} | token: ${this.token}`, sticky: false, life: 3000 }]
        await this.$router.push('/')
      } catch (error) {
        this.messages = [{ severity: 'error', content: error, sticky: false, life: 3000 }]
      }
    },
    async logout () {
      try {
        const token = localStorage.getItem('token')
        const response = await this.$axios.post('http://127.0.0.1:8000/api/logout/', null, {
          headers: {
            Authorization: `Token ${token}`
          }
        })
        localStorage.removeItem('token')
        localStorage.removeItem('username')
        this.$cookies.remove('token', { path: '/' })
        this.messages = [{ severity: response.data.type, content: response.data.message, sticky: false, life: 3000 }]
      } catch (error) {
        this.messages = [{ severity: 'error', content: error, sticky: false, life: 3000 }]
      }
    },
    tokens () {
      this.messages = [{ severity: 'warn', content: localStorage.getItem('token'), sticky: false, life: 3000 }]
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700,800,900');

a {
  cursor: pointer;
  transition: all 200ms linear;
}

a:hover {
  text-decoration: none;
}

.link {
  color: #c4c3ca;
}

.link:hover {
  color: #ffeba7;
}

p {
  font-weight: 500;
  font-size: 14px;
  line-height: 1.7;
}

h4 {
  font-weight: 600;
}

h6 span {
  padding: 0 20px;
  text-transform: uppercase;
  font-weight: 700;
}

.section {
  position: relative;
  width: 100%;
  display: block;
}

.full-height {
  min-height: 100vh;
}

[type="checkbox"]:checked,
[type="checkbox"]:not(:checked) {
  position: absolute;
  left: -9999px;
}

.checkbox:checked + label,
.checkbox:not(:checked) + label {
  position: relative;
  display: block;
  text-align: center;
  width: 60px;
  height: 16px;
  border-radius: 8px;
  padding: 0;
  margin: 10px auto;
  cursor: pointer;
  background-color: #ffeba7;
}

.checkbox:checked + label:before,
.checkbox:not(:checked) + label:before {
  position: absolute;
  display: block;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  color: #ffeba7;
  background-color: #102770;
  font-family: 'unicons';
  content: '\21F1';
  z-index: 20;
  top: -10px;
  left: -10px;
  line-height: 36px;
  text-align: center;
  font-size: 24px;
  transition: all 0.5s ease;
}

.checkbox:checked + label:before {
  transform: translateX(44px) rotate(-270deg);
}

.card-3d-wrap {
  position: relative;
  width: 440px;
  max-width: 100%;
  height: 400px;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  perspective: 800px;
  margin-top: 60px;
}

.card-3d-wrapper {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  transition: all 600ms ease-out;
}

.card-front, .card-back {
  width: 100%;
  height: 100%;
  background-color: #2a2b38;
  background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/1462889/pat.svg');
  background-position: bottom center;
  background-repeat: no-repeat;
  background-size: 300%;
  position: absolute;
  border-radius: 6px;
  left: 0;
  top: 0;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -o-backface-visibility: hidden;
  backface-visibility: hidden;
}

.card-back {
  transform: rotateY(180deg);
}

.checkbox:checked ~ .card-3d-wrap .card-3d-wrapper {
  transform: rotateY(180deg);
}

.center-wrap {
  position: absolute;
  width: 100%;
  padding: 0 35px;
  top: 50%;
  left: 0;
  transform: translate3d(0, -50%, 35px) perspective(100px);
  z-index: 20;
  display: block;
}

.form-group {
  position: relative;
  display: block;
  margin: 0;
  padding: 0;
}

.form-style {
  padding: 13px 20px;
  padding-left: 55px;
  height: 48px;
  width: 100%;
  font-weight: 500;
  border-radius: 4px;
  font-size: 14px;
  line-height: 22px;
  letter-spacing: 0.5px;
  outline: none;
  color: #c4c3ca;
  background-color: #1f2029;
  border: none;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21, 21, 21, .2);
}

.form-style:focus,
.form-style:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21, 21, 21, .2);
}

.input-icon {
  position: absolute;
  top: 0;
  left: 18px;
  height: 48px;
  font-size: 24px;
  line-height: 48px;
  text-align: left;
  color: #ffeba7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.form-group input:-ms-input-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.form-group input::-moz-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.form-group input:-moz-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.form-group input::-webkit-input-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.form-group input:focus:-ms-input-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.form-group input:focus::-moz-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.form-group input:focus:-moz-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.form-group input:focus::-webkit-input-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.btn {
  border-radius: 4px;
  height: 44px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border: none;
  background-color: #ffeba7;
  color: #102770;
  box-shadow: 0 8px 24px 0 rgba(255, 235, 167, .2);
}

.btn:active,
.btn:focus {
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16, 39, 112, .2);
}

.btn:hover {
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16, 39, 112, .2);
}

.logo {
  position: absolute;
  top: 30px;
  right: 30px;
  display: block;
  z-index: 100;
  transition: all 250ms linear;
}

.logo img {
  height: 26px;
  width: auto;
  display: block;
}
</style>
