<template>
  <div class="spinner" v-if="isLoading">
    <div class="lds-ellipsis">
      <div></div><div></div><div></div><div></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Spinner',
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

<style scoped>
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
