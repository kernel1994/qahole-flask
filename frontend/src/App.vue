<template>
  <div id="app">
    <header class="header">
      <nav class="inner">
        <div><img class="logo" src="./assets/logo-48.png" alt="logo"></div>
        <qahole-nav></qahole-nav>
      </nav>
    </header>

    <div class='wrapper'>
      <router-view :key="$route.path"/>

      <div class="spinner" v-if="isLoading">
        <div class="lds-ellipsis">
          <div></div><div></div><div></div><div></div>
        </div>
        <div>Loading...</div>
      </div>
    </div>

  </div>
</template>

<script>
import qaholeNav from './components/Nav.vue'

export default {
  name: 'App',
  components: {
    'qahole-nav': qaholeNav
  },
  data () {
    return {
      refCount: 0,
      isLoading: false
    }
  },
  methods: {
    setLoading (isLoading) {
      if (isLoading) {
        this.refCount++
        this.isLoading = true
      } else if (this.refCount > 0) {
        this.refCount--
        this.isLoading = (this.refCount > 0)
      }
    }
  },
  created () {
    this.$axios.interceptors.request.use((config) => {
      this.setLoading(true)
      return config
    }, (error) => {
      this.setLoading(false)
      return Promise.reject(error)
    })

    this.$axios.interceptors.response.use((response) => {
      this.setLoading(false)
      return response
    }, (error) => {
      this.setLoading(false)
      return Promise.reject(error)
    })
  }
}
</script>

<style>
ul {
  margin: 0;
  padding: 0;
}

.header {
  background-color: #41b883;
  position: fixed;
  z-index: 999;
  height: 55px;
  top: 0;
  left: 0;
  right: 0;
}

.header .inner {
  max-width: 800px;
  box-sizing: border-box;
  margin: 0 auto;
  padding: 10px 5px;
}

.header .inner div {
  display: inline-block;
}

.logo {
  width: 24px;
  margin-right: 10px;
  display: inline-block;
  vertical-align: middle;
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

/** https://loading.io/css/ **/
.spinner {
  margin: 0 auto;
  text-align: center;
}

.lds-ellipsis {
  display: inline-block;
  position: relative;
  width: 64px;
  height: 64px;
}
.lds-ellipsis div {
  position: absolute;
  top: 27px;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: #ddd;
  animation-timing-function: cubic-bezier(0, 1, 1, 0);
}
.lds-ellipsis div:nth-child(1) {
  left: 6px;
  animation: lds-ellipsis1 0.6s infinite;
}
.lds-ellipsis div:nth-child(2) {
  left: 6px;
  animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(3) {
  left: 26px;
  animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(4) {
  left: 45px;
  animation: lds-ellipsis3 0.6s infinite;
}
@keyframes lds-ellipsis1 {
  0% {
    transform: scale(0);
  }
  100% {
    transform: scale(1);
  }
}
@keyframes lds-ellipsis3 {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(0);
  }
}
@keyframes lds-ellipsis2 {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(19px, 0);
  }
}
</style>
