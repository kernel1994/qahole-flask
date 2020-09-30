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
          <div class="text" v-html="$convertNewLine(tucao.comment_content)"></div>
          <div class="ox">
            <span class="oo"><i class="iconfont icon-like"></i> {{ tucao.vote_positive }}</span>
            <span class="xx"><i class="iconfont icon-unlike"></i> {{ tucao.vote_negative }}</span>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Tucao',
  props: ['tucaos']
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
  padding: 0 10px;
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

.ox span {
  margin-left: 10px;
}
</style>
