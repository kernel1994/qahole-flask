<template>
  <div id="app">
    <header class="header">
      <nav class="inner">
        <router-link to="/" exact>
          <img class="logo" src="./assets/logo-2018.gif" alt="logo">
        </router-link>
        <router-link to="/random">随机</router-link>
        <router-link to="/qa">问答</router-link>
        <router-link to="/treehole">树洞</router-link>
        <input type="text" name="search" placeholder="搜索" class="search">
      </nav>
    </header>

    <div class='wrapper'>
      <router-view/>
    </div>

  </div>
</template>

<script>
export default {
  name: 'App'
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
  max-width: 800px;
  box-sizing: border-box;
  margin: 0 auto;
  padding: 7.5px 0;
}

a {
  color: #304455;
  text-decoration: none;
}

.header a:hover:not(:first-child) {
  border-bottom: 3px solid #41b883;
}

.header a.router-link-active:not(:first-child) {
  border-bottom: 3px solid #41b883;
}

.header a {
  padding-bottom: 3px;
  margin: 0 0.6em;
}

.logo {
  width: 64px;
  margin-right: 10px;
  display: inline-block;
  vertical-align: middle;
  margin-bottom: 10px;
}

.wrapper {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.search {
  float: right;

  margin-top: 5px;
  padding: 0 15px;

  border-radius: 4px;
  border: 1px solid #dcdfe6;

  height: 25px;
  box-sizing: border-box;
  color: #606266;
  cursor: pointer;
  outline: none;
  transition: border-color .2s cubic-bezier(.645,.045,.355,1);
}
</style>
