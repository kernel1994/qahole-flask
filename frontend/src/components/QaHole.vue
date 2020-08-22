<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item.comment_id">

        <div class="comment-author">
          <div class="author">{{ item.author }}</div>
          <div class="cid"># {{ item.comment_id }}</div>
          <div class="time">{{ item.comment_time }}</div>
        </div>

        <div class="comment-text">
          <div class="text" v-html="handleNewLine(item.comment_text)"></div>
          <div class="ox">
            <span class="oo"><span style="color: red;">oo</span> {{ item.oo }} | </span>
            <span class="xx"><span style="color: blue;">xx</span> {{ item.xx }} | </span>
            <span>吐槽 {{ item.ntucao }}</span>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'QaHole',
  data () {
    return {
      items: null
    }
  },

  methods: {
    handleNewLine (str) {
      return str.replace(/(?:\r\n|\r|\n)/g, '<br />')
    }
  },

  mounted () {
    let v = this
    console.log(this.$route.path)
    let url = 'http://localhost:8080/api' + this.$route.path
    this.$axios
      .get(url)
      .then(function getQaholes (response) {
        let data = null

        if (response.status === 200) {
          data = response.data
        }

        if (data.code === 0) {
          v.items = data.data
        }
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
li {
  display: flex;

  text-align: left;
  padding: 15px 10px;
  border-bottom: 1px dashed #777;
}

.comment-author {
  display: flex;
  flex-direction: column;

  min-width: 150px;
  margin-right: 10px;
}

.comment-author > .author {
  font-size: 17px;
}

.comment-author > .time, .cid {
  color: #aaa;
  font-size: 10px;
}

.comment-text {
  display: flex;
  flex-direction: column;

  min-width: 580px;
}

.comment-text > .text {
  text-align: justify;
}

.comment-text > .ox {
  padding-top: 10px;
  text-align: right;
}
</style>
