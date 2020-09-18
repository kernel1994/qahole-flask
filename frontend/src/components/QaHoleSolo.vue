<template>
  <div class="view-list">

    <div class="comment" v-if="comment">
      <div class="comment-author">
        <div class="author">{{ comment.author }}</div>
        <div>
          <div class="cid"># {{ comment.comment_id }}</div>
          <div class="time">{{ comment.comment_time }}</div>
        </div>
      </div>

      <div class="comment-text">
        <div class="text" v-html="$convertNewLine(comment.comment_text)"></div>
        <div class="ox">
          <span class="oo"><span style="color: red;">oo</span> {{ comment.oo }} | </span>
          <span class="xx"><span style="color: blue;">xx</span> {{ comment.xx }} | </span>
          <span>吐槽 {{ comment.ntucao }}</span>
        </div>
      </div>
    </div>

    <div class="tucao" v-if="tucaos">
      <ul>
        <li v-for="tucao in tucaos" :key="tucao.comment_id">

          <div class="tucao-author">
            <div class="author">{{ tucao.comment_author }}</div>
            <div class="cid"># {{ tucao.comment_id }}</div>
            <div class="time">{{ tucao.comment_date }}</div>
          </div>

          <div class="tucao-text">
            <div class="text" v-html="$convertNewLine(tucao.comment_content)"></div>
            <div class="ox">
              <span class="oo"><span style="color: red;">oo</span> {{ tucao.vote_positive }} | </span>
              <span class="xx"><span style="color: blue;">xx</span> {{ tucao.vote_negative }}</span>
            </div>
          </div>

        </li>
      </ul>
    </div>

  </div>
</template>

<script>
export default {
  name: 'QaHoleSolo',

  data () {
    return {
      comment: null,
      tucaos: null
    }
  },

  mounted () {
    let v = this

    let url = 'http://localhost:8080/api' + this.$route.path
    this.$axios
      .get(url)
      .then(function getQahole (response) {
        let data = null

        if (response.status === 200) {
          data = response.data

          if (data.code === 0) {
            v.comment = data.comment
            v.tucaos = data.tucaos
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

.view-list .comment, .tucao {
  padding: 15px 10px;
}

.comment {
  display: flex;
  flex-direction: column;

  text-align: left;
  border-bottom: 1px dashed #333;
}

.comment-author {
  display: flex;
  flex-direction: row;
  align-items: center;

  margin-bottom: 10px;
}

.comment-author .author {
  font-size: 20px;
  margin-right: 10px;
}

.time, .cid {
  color: #aaa;
  font-size: 10px;
}

.comment-text {
  display: flex;
  flex-direction: column;
}

.text {
  text-align: justify;
  margin-bottom: 10px;
}

.comment-text > .ox {
  text-align: right;
}

.ox a {
  color: #333;
  text-decoration: none;
}

.tucao {
  margin-bottom: 10px;
}

li {
  display: flex;

  list-style-type: none;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

li:not(:last-child) {
  border-bottom: 1px dashed #777;
}

.tucao-author {
  min-width: 100px;
  margin-right: 10px;
}

.tucao-text {
  flex-grow: 1;
}

.tucao-text > .ox {
  text-align: right;
}
</style>
