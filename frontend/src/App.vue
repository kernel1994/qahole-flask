<template>
  <div id="app" class='wrapper'>
    <h4>Qa & Treehole</h4>
    <div>
      <qahole-nav></qahole-nav>
    </div>

    <router-view :key="$route.path"/>

    <div v-if="isLoading">
      <div class="lds-ellipsis">
        <div></div><div></div><div></div><div></div>
      </div>
      <div>Loading...</div>
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

/** https://loading.io/css/ **/
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
