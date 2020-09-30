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
              <span class="oo"><i class="iconfont icon-like"></i> {{ comment.oo }}</span>
              <span class="xx"><i class="iconfont icon-unlike"></i> {{ comment.xx }}</span>
              <span>
                <a href="javascript:void(0)" @click="tucao(comment.comment_id)">
                 <i class="iconfont icon-comment"></i> {{ comment.ntucao }}
               </a>
              </span>
            </div>
          </div>
        </div>

        <div class="tucao">
          <div :data-comment-tucao-id="comment.comment_id" class="tucao-list" showed="false">
            <!-- tucao list mounted here -->
          </div>
        </div>

      </li>
    </ul>
  </div>
</template>

<script>
import Vue from 'vue'
import Tucao from '@/components/Tucao'
import Spinner from '@/components/Spinner'

export default {
  name: 'QaHole',

  components: {
    Tucao,
    Spinner
  },

  data () {
    return {
      loading: true,
      comments: null,
      tucaos: null
    }
  },

  methods: {
    tucao (commentParentId) {
      let tucaoParent = document.querySelector(`div[data-comment-tucao-id='${commentParentId}']`)
      let showed = tucaoParent.getAttribute('showed')

      if (showed === 'true') {
        // TODO: 更好的销毁组件的方式
        tucaoParent.removeChild(tucaoParent.firstChild)
        tucaoParent.setAttribute('showed', false)
        return
      }

      // display spinner
      let SpinnerComp = Vue.extend(Spinner)

      let spinnerInstance = new SpinnerComp({
        propsData: {
          show: true
        }
      })

      spinnerInstance.$mount()
      tucaoParent.appendChild(spinnerInstance.$el)
      // spinner displayed

      let url = 'http://localhost:8080/api/tucao/' + commentParentId
      this.$axios
        .get(url)
        .then(response => {
          if (response.status === 200) {
            let data = response.data

            if (data.code === 0) {
              let TucaoComp = Vue.extend(Tucao)

              let tucaoInstance = new TucaoComp({
                propsData: {
                  tucaos: data.data
                }
              })

              tucaoInstance.$mount()
              tucaoParent.appendChild(tucaoInstance.$el)

              tucaoParent.setAttribute('showed', true)

              // spinner disappear
              // TODO: 更好的销毁组件的方式
              tucaoParent.removeChild(spinnerInstance.$el)
            }
          }
        })
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
            this.comments = data.data

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

li {
  list-style-type: none;
}

li:not(:last-child) {
  border-bottom: 1px dashed #777;
}

.comment {
  display: flex;

  text-align: left;
  padding: 15px 10px 0;
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

.ox span {
  margin-left: 10px;
}

.tucao {
  margin-bottom: 10px;
}

.cid a {
  color: #333;
  text-decoration: none;
}
</style>
