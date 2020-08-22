<template>
  <div id="app" class='wrapper'>
    <h4>Qa & Treehole</h4>
    <div>
      <qahole-nav></qahole-nav>
    </div>
    <router-view :key="$route.path"/>
  </div>
</template>

<script>
import qaholeNav from './components/Nav.vue'

export default {
  name: 'App',
  components: {
    'qahole-nav': qaholeNav
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.wrapper {
  width: 100%;
  max-width: 50rem;
  margin: 0 auto;
}
</style>
