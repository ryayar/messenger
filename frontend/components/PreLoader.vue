<template>
  <div class="preloader">
    <div class="animated-sun">
      🔆️
    </div>
    <div class="animated-cloud">
      🌥️️
    </div>
    <div class="animated-rain">
      🌧️
    </div>
    <div class="animated-umbrella">
      ☔️
    </div>
    <div class="animated-thunderstorm">
      ⛈️
    </div>
    <div class="animated-snow">
      ❄️
    </div>
    <div class="animated-fog">
      🌫️
    </div>
  </div>
</template>

<script>
export default {
  name: 'PreLoader'
}
</script>

<style scoped>
.preloader {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100dvh;
  background-color: var(--preloader-color);
  color: #fff;
  cursor: default;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 9999;
}

.animated-sun, .animated-rain, .animated-thunderstorm, .animated-fog, .animated-cloud, .animated-umbrella, .animated-snow {
  font-size: calc(var(--fs-h1-text)*3);
  /*scale: calc(var(--fs-h1-text)*3);*/
  margin: 0 10px;
  filter: drop-shadow(0 0 20px var(--drop-shadow));
  /*transition: all 0.5s ease;*/
}

.animated-sun, .animated-rain, .animated-thunderstorm, .animated-fog {
  animation: emojiAnimation-even 1s infinite ease-in;
}

@keyframes emojiAnimation-even {
  0% {
    transform: translateY(100px);
  }
  50% {
    transform: scale(1.5) translateY(-100px);
  }
  100% {
    transform: translateY(100px);
  }
}

.animated-cloud, .animated-umbrella, .animated-snow {
  animation: emojiAnimation-odd 1s infinite ease-in;
}

@keyframes emojiAnimation-odd {
  0% {
    transform: scale(1.5) translateY(-100px);
  }
  50% {
    transform: translateY(100px);
  }
  100% {
    transform: scale(1.5) translateY(-100px);
  }
}
</style>
