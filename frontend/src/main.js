// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

Vue.prototype.$axios = axios
Vue.config.productionTip = false

// 全局函数，替换 JSON 中换行符为 HTML 的 <br />
Vue.prototype.$convertNewLine = function (str) {
  return str.replace(/(?:\r\n|\r|\n)/g, '<br />')
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
