<template>
  <div class="nav">
    <ul>
      <li v-for="(item, index) in items" :key="item.text">
        <a :href="item.href"
           :class="[commonClass, item.active ? activeClass : '']"
           v-on:click="navClickEvent(items,index)">
        <span class="nav-txt">{{ item.text }}</span>
      </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'qahole-nav',

  data: function () {
    return {
      commonClass: 'nav-link',
      activeClass: 'current',
      items: [
        {
          text: '首页',
          href: '#/',
          active: true
        },

        {
          text: '问答',
          href: '#/qa',
          active: false
        },

        {
          text: '树洞',
          href: '#/treehole',
          active: false
        }
      ]
    }
  },

  methods: {
    navClickEvent: function (items, index) {
      /* 默认切换类的动作 */
      items.forEach(function (el) {
        el.active = false
      })

      items[index].active = true

      /* 开放用户自定义的接口 */
      this.$emit('navClickEvent', items, index)
    }
  }
}
</script>

<style scoped>
  @import '../assets/css/nav.css';
</style>
