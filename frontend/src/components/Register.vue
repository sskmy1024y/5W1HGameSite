<template>
  <el-dialog title="登録" :visible.sync="isDialogVisible" width="90%" center>
    <span>キーワードを登録します</span>
    <section>
      <div class="register" style="text-align:center">
        <el-form :inline="true" :model="form" label-width="100px">
          <el-form-item label="いつ">
            <el-input v-model="form.when" placeholder="昨日" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" @click="addWord('when')">追加</el-button>
        </el-form>

        <el-form :inline="true" :model="form" label-width="100px">
          <el-form-item label="どこで">
            <el-input v-model="form.where" placeholder="工科大で" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" @click="addWord('where')">追加</el-button>
        </el-form>

        <el-form :inline="true" :model="form" label-width="100px">
          <el-form-item label="誰が">
            <el-input v-model="form.who" placeholder="ポプ子とピピ美が" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" @click="addWord('who')">追加</el-button>
        </el-form>

        <el-form :inline="true" :model="form" label-width="100px">
          <el-form-item label="何を">
            <el-input v-model="form.what" placeholder="竹書房を" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" @click="addWord('what')">追加</el-button>
        </el-form>

        <el-form :inline="true" :model="form" label-width="100px">
          <el-form-item label="なぜ">
            <el-input v-model="form.why" placeholder="気紛れで" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" @click="addWord('why')">追加</el-button>
        </el-form>

        <el-form :inline="true" :model="form" label-width="100px">
          <el-form-item label="どうした">
            <el-input v-model="form.how" placeholder="土に埋めた" style="width:300px"></el-input>
          </el-form-item>
          <el-button type="primary" @click="addWord('how')">追加</el-button>
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
        whet: '',
        why: '',
        how: ''
      },
      newWho: '',
      newWhen: '',
      newWhere: '',
      newWhat: '',
      newWhy: '',
      newHow: '',
      errored: false,
      isDialogVisible: false
    };
  },
  methods: {
    addWord: function(type) {
      const headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*'
      };
      let word = '';
      switch (type) {
        case 'who':
          word = this.newWho;
          this.newWho = '';
          break;

        case 'when':
          word = this.newWhen;
          this.newWhen = '';
          break;

        case 'where':
          word = this.newWhere;
          this.newWhere = '';
          break;

        case 'what':
          word = this.newWhat;
          this.newWhat = '';
          break;

        case 'why':
          word = this.newWhy;
          this.newWhy = '';
          break;

        case 'how':
          word = this.newHow;
          this.newHow = '';
          break;
      }

      if (word === '') {
        alert(
          `${type}に文章が指定されずに追加ボタンが押されました！エラーです！`
        );
        return false;
      }

      axios
        .post(`http://localhost:8000/api/${type}`, word, headers)
        .then(() => {
          alert(`「${word}」が${type}に登録されました`);
        })
        .catch(() => {
          alert(`「${word}」は既に${type}に登録されています！`);
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
