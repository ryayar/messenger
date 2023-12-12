<template>
  <div id="app" class="site">
    <IndexComponent />
  </div>
</template>

<script>
import IndexComponent from '~/components/Index/IndexComponent'
export default {
  name: 'IndexPage',
  components: {
    IndexComponent
  },
  data () {
    return {
      isLoading: true,
      effects: null,
      username: ''
    }
  },
  mounted () {
    this.username = localStorage.getItem('username')
  //   setTimeout(() => {
  //     this.isLoading = false
  //   }, 3000)
  },
  methods: {
    weatherEffect (data) {
      this.effects = data
      setTimeout(() => {
        this.isLoading = false
      }, 1000)
    }
  }
}
</script>
