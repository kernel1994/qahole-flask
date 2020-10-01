import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import QaHoleSolo from '@/components/QaHoleSolo'

Vue.use(Router)

const createListView = id => () => import('@/components/createListView').then(m => m.default(id))

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },

    {
      path: '/random',
      name: 'QaHole',
      component: createListView('random')
    },

    {
      path: '/qahole/:id',
      name: 'QaHoleSolo',
      component: QaHoleSolo
    },

    {
      path: '/qa',
      name: 'Qa',
      component: createListView('qa'),
      children: [
        {
          path: ':id'
        }
      ]
    },

    {
      path: '/treehole',
      name: 'Treehole',
      component: createListView('treehole'),
      children: [
        {
          path: ':id'
        }
      ]
    }
  ]
})
