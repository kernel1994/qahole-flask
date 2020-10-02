// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import titleMixin from './util/title'
import ProgressBar from '@/components/ProgressBar.vue'

import '@/assets/iconfont/iconfont.css'

// mixin for handling title
Vue.mixin(titleMixin)

Vue.prototype.$axios = axios
Vue.config.productionTip = false

// 全局函数，替换 JSON 中换行符为 HTML 的 <br />
Vue.prototype.$convertNewLine = function (str) {
  return str.replace(/(?:\r\n|\r|\n)/g, '<br />')
}

// global progress bar
const bar = Vue.prototype.$bar = new Vue(ProgressBar).$mount()
document.body.appendChild(bar.$el)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
