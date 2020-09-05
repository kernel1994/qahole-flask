<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul>
      <li>
        <a href="#/qa">问答</a>
      </li>
      <li>
        <a href="#/treehole">树洞</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  margin-top: 55px;
}

h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
