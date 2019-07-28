<template>
<div class="register_word">
    <section>
        <div class="register">
            <h2>登録</h2>
            <form v-on:submit.prevent>
                <input type="text" v-model="newWho" placeholder="誰が">
                <button @click="addWord('who')">
                    Add Who
                </button>
                <input type="text" v-model="newWhen" placeholder="いつ">
                <button @click="addWord('when')">
                    Add When
                </button>
                <input type="text" v-model="newWhere" placeholder="どこで">
                <button @click="addWord('where')">
                    Add Where
                </button>
                <input type="text" v-model="newWhat" placeholder="なにを">
                <button @click="addWord('what')">
                    Add What
                </button>
                <input type="text" v-model="newWhy" placeholder="なぜ">
                <button @click="addWord('why')">
                    Add Why
                </button>
                <input type="text" v-model="newHow" placeholder="どのようにした">
                <button @click="addWord('how')">
                    Add How
                </button>
            </form>
        </div>
    </section>

    <section>
        <div class="page-link">
            <router-link to="/">トップページに戻る</router-link>
        </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'register_word',
  data () {
    return {
      newWho: '',
      newWhen: '',
      newWhere: '',
      newWhat: '',
      newWhy: '',
      newHow: '',
      errored: false,
      headers: {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*'
      }
    }
  },

  methods: {
    addWord: function (type) {
      let word = ''

      switch (type) {
        case 'who':
          word = this.newWho
          this.newWho = ''
          break

        case 'when':
          word = this.newWhen
          this.newWhen = ''
          break

        case 'where':
          word = this.newWhere
          this.newWhere = ''
          break

        case 'what':
          word = this.newWhat
          this.newWhat = ''
          break

        case 'why':
          word = this.newWhy
          this.newWhy = ''
          break

        case 'how':
          word = this.newHow
          this.newHow = ''
          break
      }

      if (word === '') {
        alert(`${type}に文章が指定されずに追加ボタンが押されました！エラーです！`)
        return
      }

      axios
        .post(`http://localhost:8000/api/${type}`, {'word': word}, this.headers)
        .then((response) => {
          console.log('OK', response)
          alert(`「${word}」が${type}に登録されました`)
        })
        .catch((err) => {
          console.log('word not found', err)
          alert(`「${word}」は既に${type}に登録されています！`)
        })
    }
  }
}
</script>

<style scoped>
h1, h2 {
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
