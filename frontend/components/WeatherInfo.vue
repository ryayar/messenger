<template>
  <div class="wrapper">
    <p class="h1">
      Узнать погоду в {{ city === '' ? 'вашем городе' : 'городе: ' + cityName }}
    </p>
    <input v-model="city" type="text" placeholder="Введите город" @keydown.enter="getWeather()">
    <button v-if="city !== ''" @click="getWeather()">
      Узнать погоду
    </button>
    <button v-else disabled>
      Введите название города
    </button>
    <p v-if="error != null" class="error">
      {{ error }}
    </p>
    <div class="info">
      <transition name="card-info">
        <div v-if="info" class="card-info">
          <div class="card-info__clouds">
            {{ showClouds }}
          </div>
          <div class="card-info__now">
            {{ showTemp }}
          </div>
          <div class="card-info__fells-like">
            {{ showFeelsLike }}
          </div>
          <div class="card-info__temp">
            <div class="card-info__temp-min">
              {{ showMinTemp }}
            </div>
            <div class="card-info__temp-splitter">
              |
            </div>
            <div class="card-info__temp-max">
              {{ showMaxTemp }}
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'WeatherInfo',
  data () {
    return {
      city: '',
      error: null,
      info: null,
      weatherDescriptionToParallax: null
    }
  },
  computed: {
    cityName () {
      const city = this.city[0].toUpperCase() + this.city.slice(1)
      return '«' + city + '»'
    },
    showTemp () {
      return `${Math.ceil(this.info.main.temp)}°C`
    },
    showFeelsLike () {
      return `Ощущается как: ${Math.ceil(this.info.main.feels_like)}°C`
    },
    showMinTemp () {
      return `↓ ${Math.ceil(this.info.main.temp_min)}°C`
    },
    showMaxTemp () {
      return `↑ ${Math.ceil(this.info.main.temp_max)}°C`
    },
    showClouds () {
      const weatherDescription = this.info.weather[0].main
      /* eslint-disable */
      const codeToSmile = {
        'Clear': '🔆️',
        'Clouds': '🌥️️',
        'Rain': '🌧️',
        'Drizzle': '☔️',
        'Thundershtorm': '⛈️',
        'Snow': '❄️',
        'Mist': '🌫️',
        'Fog': '🌫️',
        'Haze': '🌫️'
      }
      if (weatherDescription in codeToSmile) {
        this.weatherDescriptionToParallax = weatherDescription
        return codeToSmile[weatherDescription]
      } else {
        return  weatherDescription
      }
    }
  },
  methods: {
    getWeather () {
      if (this.city.trim().length < 2) {
        this.error = 'Нужно название более одного символа'
        return false
      }

      this.error = ''
      this.info = null

      axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${this.city}&units=metric&appid=f3d3849c3d17603d9f5b4665d3a00d99`)
        .then(res => {
          this.info = res.data
          this.$emit('weatherEffect', res.data.weather[0].main)
        })
        .catch(error => (this.error = 'Такого города не существует'))
    }
  },
  mounted () {
    axios.get('http://ip-api.com/json/?fields=city&lang=ru')
    .then(response => {
      this.city = response.data.city
      this.getWeather()
    })
    .catch(error => {
      console.error('Ошибка при получении города по IP:', error)
    })
  }
}
</script>

<style scoped>
.h1 {
  font-size: clamp(var(--fs-h1-text), 3vw, calc(var(--fs-h1-text)*1.1));
  cursor: default;
}
.wrapper {
  flex: 1;
  border-radius: 3em;
  padding: 5vh 2vh;
  /*background: rgba(93, 69, 43, 0.8);*/
  background: var(--wrapper-bg-color);
  box-shadow: 0 0 5em 1em var(--wrapper-border-color);
  text-align: center;
  color: #fcfcfc;
  transition: 0.5s ease;
  z-index: 10;
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

.info {
  display: flex;
  justify-content: center;
}

.card-info {
  cursor: default;
}

.card-info__clouds {
  font-size: calc(var(--fs-h1-text) * 3.3);
}

.card-info__now {
  font-size: calc(var(--fs-h1-text) * 1.5);
}

.card-info__fells-like, .card-info__temp, .wrapper input, .wrapper button {
  font-size: calc(var(--fs-text) * 1.8);
}

.card-info__temp {
  margin-top: 0.5em;
  display: flex;
  justify-content: space-between;
}

input, .wrapper button, .h1, .card-info__clouds, .card-info__now, .card-info__fells-like, .card-info__temp-min, .card-info__temp-max {
  transition: all 0.5s ease;
}

input:hover, .wrapper button:hover, .h1:hover, .card-info__clouds:hover, .card-info__now:hover, .card-info__fells-like:hover, .card-info__temp-min:hover, .card-info__temp-max:hover {
  transform: scale(1.1) translateY(-5px);
  filter: drop-shadow(0 0 20px var(--drop-shadow));
}

.card-info-enter-active, .card-info-leave-active {
  transition: all 0.7s; /* Время анимации */
}
.card-info-enter, .card-info-leave-to /* .card-info-leave-active в версии < 2.1.8 */ {
  opacity: 0;
  transform: translateX(100%); /* Начальное положение новой информации за пределами экрана справа */
}
.card-info-leave, .card-info-enter-to /* .card-info-enter-active в версии < 2.1.8 */ {
  opacity: 0;
  transform: translateX(-100%); /* Конечное положение текущей информации за пределами экрана слева */
}

.error {
  color: #d03939;
}
</style>
