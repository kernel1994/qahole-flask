<template>
  <div class="view-list">

    <div class="comment" v-if="comment">
      <div class="comment-author">
        <div class="author">{{ comment.author }}</div>
        <div class="cid"># {{ comment.comment_id }}</div>
      </div>

      <div class="comment-text">
        <div class="text" v-html="$convertNewLine(comment.comment_text)"></div>
        <div class="ox">
          <div class="time">{{ comment.comment_time }}</div>
          <span class="oo"><i class="iconfont icon-like"></i> {{ comment.oo }}</span>
          <span class="xx"><i class="iconfont icon-unlike"></i> {{ comment.xx }}</span>
          <span><i class="iconfont icon-comment"></i> {{ comment.ntucao }}</span>
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
              <span class="oo"><i class="iconfont icon-like"></i> {{ tucao.vote_positive }}</span>
              <span class="xx"><i class="iconfont icon-unlike"></i> {{ tucao.vote_negative }}</span>
            </div>
          </div>

        </li>
      </ul>

      <i class="no-tucaos" v-if="tucaos.length === 0">There are no Tucaos</i>
    </div>

  </div>
</template>

<script>
export default {
  name: 'QaHoleSolo',

  title () {
    return this.$route.path.slice(1).split('/').join(' | ')
  },

  data () {
    return {
      comment: null,
      tucaos: null
    }
  },

  mounted () {
    let url = 'http://localhost:8080/api' + this.$route.path
    this.$bar.start()
    this.$axios
      .get(url)
      .then((response) => {
        let data = null

        if (response.status === 200) {
          data = response.data

          if (data.code === 0) {
            this.comment = data.comment
            this.tucaos = data.tucaos

            this.$bar.finish()
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
  border-bottom: 1px solid #333;
}

.comment-author {
  display: flex;
  flex-direction: row;
  align-items: center;

  margin-bottom: 10px;
}

.comment-author .author {
  flex-grow: 1;

  font-size: 20px;
}

.time, .cid {
  color: #aaa;
  font-size: 10px;
}

.comment-text {
  display: flex;
  flex-direction: column;
}

.comment .ox {
  display: flex;
  align-items: center;
}

.comment .ox .time {
  flex-grow: 1;
}

.text {
  text-align: justify;
  margin-bottom: 10px;
}

.ox span {
  margin-left: 10px;
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
  min-width: 120px;
  max-width: 120px;
  margin-right: 10px;
}

.tucao-text {
  flex-grow: 1;
}

.tucao-text > .ox {
  text-align: right;
}

.tucao .no-tucaos {
  color: gray;
}
</style>
