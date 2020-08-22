import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import QaHole from '@/components/QaHole'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },

    {
      path: '/qahole',
      name: 'QaHole',
      component: QaHole
    },

    {
      path: '/qa',
      name: 'Qa',
      component: QaHole,
      children: [
        {
          path: ':id'
        }
      ]
    },

    {
      path: '/treehole',
      name: 'Treehole',
      component: QaHole,
      children: [
        {
          path: ':id'
        }
      ]
    }
  ]
})
