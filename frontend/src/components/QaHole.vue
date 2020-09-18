<template>
  <div class="view-list">
    <ul>
      <li v-for="comment in comments" :key="comment.comment_id">

        <div class="comment">
          <div class="comment-author">
            <div class="author">{{ comment.author }}</div>
            <div class="cid">
              <a :href="'#/qahole/' + comment.comment_id"># {{ comment.comment_id }}</a>
            </div>
            <div class="time">{{ comment.comment_time }}</div>
          </div>

          <div class="comment-text">
            <div class="text" v-html="$convertNewLine(comment.comment_text)"></div>
            <div class="ox">
              <span class="oo"><span style="color: red;">oo</span> {{ comment.oo }} | </span>
              <span class="xx"><span style="color: blue;">xx</span> {{ comment.xx }} | </span>
              <span>
                <a href="javascript:void(0)" @click="tucao(comment.comment_id)">吐槽 {{ comment.ntucao }}</a>
              </span>
            </div>
          </div>
        </div>

        <div class="tucao">
          <div :data-comment-tucao-id="comment.comment_id" class="tucao-list" showed="false">
            <div></div>
          </div>
        </div>

      </li>
    </ul>
  </div>
</template>

<script>
import Vue from 'vue'
import Tucao from '@/components/Tucao'

export default {
  name: 'QaHole',
  data () {
    return {
      comments: null,
      tucaos: null
    }
  },

  methods: {
    tucao (commentParentId) {
      let parent = document.querySelector(`div[data-comment-tucao-id='${commentParentId}']`)
      let showed = parent.getAttribute('showed')

      if (showed === 'true') {
        parent.querySelector('div').innerHTML = ''
        parent.setAttribute('showed', false)
        return
      }

      let TucaoComp = Vue.extend({
        components: { Tucao },
        template: `<Tucao commentParentId="${commentParentId}"></Tucao>`
      })

      new TucaoComp().$mount(`div[data-comment-tucao-id='${commentParentId}'] > div`)

      parent.setAttribute('showed', true)
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

          if (data.code === 0) {
            v.comments = data.data
          }
        }
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.view-list {
  margin-top: 70px;
  padding: 0 20px;
  background-color: #fff;
  border-radius: 2px;
  transition: all .5s cubic-bezier(.55, 0, .1, 1);
}

li {
  list-style-type: none;
}

li:not(:last-child) {
  border-bottom: 1px dashed #777;
}

.comment {
  display: flex;

  text-align: left;
  padding: 15px 10px;
}

.comment-author {
  display: flex;
  flex-direction: column;

  width: 150px;
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

  width: 620px;
}

.comment-text > .text {
  text-align: justify;
}

.comment-text > .ox {
  padding-top: 10px;
  text-align: right;
}

.ox a {
  color: #333;
  text-decoration: none;
}

.tucao {
  margin-bottom: 10px;
}

.cid a {
  color: #333;
  text-decoration: none;
}
</style>
