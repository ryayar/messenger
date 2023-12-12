<template>
  <div>
    <AppHeader />
    <Nuxt />
    <AppFooter />
  </div>
</template>
<script>
import AppHeader from '~/layouts/AppHeader'
import AppFooter from '~/layouts/AppFooter'
export default {
  components: {
    AppFooter, AppHeader
  }
}
</script>
