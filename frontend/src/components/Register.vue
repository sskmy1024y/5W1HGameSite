<template>
  <el-dialog title="登録" :visible.sync="isDialogVisible" width="90%" center>
    <section style="text-align:center">
      <span>キーワードを登録します</span>
      <div class="register">
        <el-form
          :inline="true"
          :model="form"
          @submit.native.prevent="addWord('when')"
          label-width="100px"
        >
          <el-form-item label="いつ">
            <el-input v-model="form.when" placeholder="昨日" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" native-type="submit">追加</el-button>
        </el-form>

        <el-form
          :inline="true"
          :model="form"
          label-width="100px"
          @submit.native.prevent="addWord('where')"
        >
          <el-form-item label="どこで">
            <el-input v-model="form.where" placeholder="工科大で" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" native-type="submit">追加</el-button>
        </el-form>

        <el-form
          :inline="true"
          :model="form"
          label-width="100px"
          @submit.native.prevent="addWord('who')"
        >
          <el-form-item label="誰が">
            <el-input v-model="form.who" placeholder="ポプ子とピピ美が" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" native-type="submit">追加</el-button>
        </el-form>

        <el-form
          :inline="true"
          :model="form"
          label-width="100px"
          @submit.native.prevent="addWord('what')"
        >
          <el-form-item label="何を">
            <el-input v-model="form.what" placeholder="竹書房を" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" native-type="submit">追加</el-button>
        </el-form>

        <el-form
          :inline="true"
          :model="form"
          label-width="100px"
          @submit.native.prevent="addWord('why')"
          v-if="false"
        >
          <el-form-item label="なぜ">
            <el-input v-model="form.why" placeholder="気紛れで" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" native-type="submit">追加</el-button>
        </el-form>

        <el-form
          :inline="true"
          :model="form"
          label-width="100px"
          @submit.native.prevent="addWord('how')"
        >
          <el-form-item label="どうした">
            <el-input v-model="form.how" placeholder="土に埋めた" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" native-type="submit">追加</el-button>
        </el-form>
      </div>
    </section>
    <span slot="footer" class="dialog-footer">
      <el-button @click="isDialogVisible = false">閉じる</el-button>
    </span>
  </el-dialog>
</template>

<script>
import axios from 'axios';
export default {
  name: 'register_word',
  data() {
    return {
      form: {
        who: '',
        when: '',
        where: '',
        what: '',
        why: '',
        how: ''
      },
      errored: false,
      isDialogVisible: false
    };
  },
  methods: {
    addWord: function(type) {
      if (type === '') return false;

      const headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*'
      };
      const word = this.form[type];

      if (word === '') {
        this.$message({
          message: `${type}に文章が指定されずに追加ボタンが押されました！エラーです！`,
          type: 'error'
        });
        return false;
      }

      axios
        .post(
          `http://${process.env.VUE_APP_API_HOST}/api/${type}`,
          { word: word },
          headers
        )
        .then(() => {
          this.form[type] = '';
          this.$message({
            message: `「${word}」が${type}に登録されました`,
            type: 'success'
          });
        })
        .catch(err => {
          switch (err.response.status) {
            case 409:
              this.$message({
                message: `「${word}」は既に${type}に登録されています！`,
                type: 'error'
              });
              break;
            case 500:
              this.$message({
                message: 'サーバー側でエラーが発生しました。',
                type: 'error'
              });
              break;
            default:
              this.$message({
                message: '不明なエラーが発生しました。',
                type: 'error'
              });
          }
        });
    },
    dialog: function(bool) {
      this.isDialogVisible = bool;
    }
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
</style>
