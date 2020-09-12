<template>
  <div id="app">
    <header class="header">
      <nav class="inner">
        <img class="logo" src="./assets/logo-2018.gif" alt="logo">
        <qahole-nav class="qahole-nav"></qahole-nav>
        <input type="text" name="search" placeholder="搜索" class="search">
      </nav>
    </header>

    <div class='wrapper'>
      <router-view :key="$route.path"/>

      <spinner></spinner>
    </div>

  </div>
</template>

<script>
import Spinner from '@/components/Spinner'
import qaholeNav from '@/components/Nav.vue'

export default {
  name: 'App',
  components: {
    'qahole-nav': qaholeNav,
    'spinner': Spinner
  }
}
</script>

<style>
body {
  background-color: #f2f3f5;
}

ul {
  margin: 0;
  padding: 0;
}

.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 999;
  height: 55px;
  background-color: #fff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, .1);
}

.header .inner {
  display: flex;
  align-items: center;

  max-width: 800px;
  box-sizing: border-box;
  margin: 0 auto;
  padding: 7.5px 0;
}

.inner .qahole-nav {
  flex-grow: 1;
}

.logo {
  width: 64px;
  margin-right: 10px;
  display: inline-block;
  vertical-align: middle;
  margin-bottom: 10px;
}

.header .github {
  color: #fff;
  font-size: 0.9em;
  margin: 0;
  float: right;
}

.wrapper {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.search {
  cursor: pointer;
  border-radius: 4px;
  border: 1px solid #dcdfe6;
  box-sizing: border-box;
  color: #606266;
  height: 25px;
  outline: none;
  padding: 0 15px;
  transition: border-color .2s cubic-bezier(.645,.045,.355,1);
}
</style>
