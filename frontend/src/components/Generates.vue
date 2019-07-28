<template>
  <el-dialog
    title="イツドコゲーム！"
    :visible.sync="isDialogVisible"
    width="90%"
    center
    :close-on-click-modal="false"
    :show-close="false"
  >
    <section style="text-align:center">
      <span>みんなの登録したキーワードから、文章が作られるよ！</span>
      <div class="contents">
        <el-button
          v-if="-3 < status && status < 0"
          type="primary"
          :loading="status==-1"
          @click="start"
        >スタート！</el-button>

        <el-steps v-if="status >= 0" :active="status" align-center>
          <el-step title="いつ" :description="contents.when.word" :status="contents.when.status"></el-step>
          <el-step title="どこで" :description="contents.where.word" :status="contents.where.status"></el-step>
          <el-step title="だれが" :description="contents.who.word" :status="contents.who.status"></el-step>
          <el-step title="なにを" :description="contents.what.word" :status="contents.what.status"></el-step>
          <el-step title="どうした" :description="contents.how.word" :status="contents.how.status"></el-step>
        </el-steps>

        <h1
          class="result"
        >{{`${contents.when.word}${contents.where.word}${contents.who.word}${contents.what.word}${contents.how.word}`}}</h1>
      </div>
    </section>
    <span slot="footer" class="dialog-footer">
      <el-button v-if="status == 5 || status == -2" @click="isDialogVisible = false">閉じる</el-button>
      <el-button
        type="primary"
        v-if="status > 4 || status == -3"
        :loading="status==-3"
        @click="restart"
      >もう一度</el-button>
    </span>
  </el-dialog>
</template>

<script>
import axios from 'axios';
export default {
  name: 'generate_sentence',
  data() {
    return {
      contents: {
        who: {
          word: '',
          status: 'waiting'
        },
        when: {
          word: '',
          status: 'waiting'
        },
        where: {
          word: '',
          status: 'waiting'
        },
        what: {
          word: '',
          status: 'waiting'
        },
        why: {
          word: '',
          status: 'waiting'
        },
        how: {
          word: '',
          status: 'waiting'
        }
      },
      initialContents: {},
      status: -2,
      errored: false,
      isDialogVisible: false
    };
  },
  methods: {
    start: function() {
      this.status = -1;
      setTimeout(() => {
        this.status = 0;
        setTimeout(() => {
          this.sequence();
        }, 1500);
      }, 1000);
    },

    restart: function() {
      this.contents = this.initialContents;
      this.status = -3;
      setTimeout(() => {
        this.status = 0;
        setTimeout(() => {
          this.sequence();
        }, 1500);
      }, 1000);
    },

    sequence: function() {
      const words = ['when', 'where', 'who', 'what', 'how'];

      words.forEach((type, index) => {
        setTimeout(() => {
          if (words.length - 1 > index)
            this.contents[words[index + 1]].status = 'process';
          this.getWord(type);
        }, 1500 * index);
      });
    },

    getWord: function(type) {
      if (type === '') return false;

      const headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*'
      };

      axios
        .get(`http://${process.env.VUE_APP_API_HOST}/api/${type}`, headers)
        .then(response => {
          if (response.data.word) this.contents[type].word = response.data.word;
          this.contents[type].status = 'success';
          this.status++;
        })
        .catch(err => {
          this.$message({
            message: 'サーバーエラーが発生しました!',
            type: 'error'
          });
          this.contents[type].status = 'error';
          this.status++;
        });
    },
    dialog: function(bool) {
      this.isDialogVisible = bool;
    }
  },
  mounted() {
    this.initialContents = this.contents;
  }
};
</script>

<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.contents {
  margin: 30px;
}

.result {
  font-weight: bold;
  margin-top: 60px;
}
</style>
