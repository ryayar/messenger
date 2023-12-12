<template>
  <nav>
    <NuxtLink to="/">
      Home page
    </NuxtLink>
    |
    <NuxtLink to="/about">
      About page
    </NuxtLink>
    |
    <NuxtLink to="/contacts">
      Contacts page
    </NuxtLink>
  </nav>
</template>

<script>
export default {
  name: 'NavComponent'
}
</script>

<style scoped>

</style>
