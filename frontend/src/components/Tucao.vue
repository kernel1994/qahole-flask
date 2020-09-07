<template>
  <div class="tucao-list">
    <ul>
      <li v-for="tucao in tucaos" :key="tucao.comment_id">

        <div class="tucao-author">
          <div class="author">{{ tucao.comment_author }}</div>
          <div class="cid"># {{ tucao.comment_id }}</div>
          <div class="time">{{ tucao.comment_date }}</div>
        </div>

        <div class="tucao-text">
          <div class="text" v-html="handleNewLine(tucao.comment_content)"></div>
          <div class="ox">
            <span class="oo"><span style="color: red;">oo</span> {{ tucao.vote_positive }} | </span>
            <span class="xx"><span style="color: blue;">xx</span> {{ tucao.vote_negative }} | </span>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Tucao',
  data () {
    return {
      tucaos: null
    }
  },

  props: {
    commentParentId: {
      type: String
    }
  },

  methods: {
    handleNewLine (str) {
      return str.replace(/(?:\r\n|\r|\n)/g, '<br />')
    }
  },

  mounted () {
    let v = this

    let url = 'http://localhost:8080/api/tucao/' + v.commentParentId
    this.$axios
      .get(url)
      .then(function getQaholes (response) {
        let data = null

        if (response.status === 200) {
          data = response.data

          if (data.code === 0) {
            v.tucaos = data.data
          }
        }
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tucao-list {
  display: flex;
  justify-content: flex-end;
}

ul {
  width: 650px;
  background-color: #f2f2f2;
  border-color: #d9d9d9;
}

li {
  display: flex;
  text-align: left;
  padding: 15px 10px;
  border-bottom: 1px solid #777;
}

.tucao-author {
  display: flex;
  flex-direction: column;

  width: 150px;
  margin-right: 10px;
}

.tucao-author > .author {
  font-size: 17px;
}

.tucao-author > .time, .cid {
  color: #aaa;
  font-size: 10px;
}

.tucao-text {
  display: flex;
  flex-direction: column;

  width: 620px;
}

.tucao-text > .text {
  text-align: justify;
}

.tucao-text > .ox {
  padding-top: 10px;
  text-align: right;
}
</style>
