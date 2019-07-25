<template>
<div class="register_word">
    <section>
        <div class="register">
            <h2>登録</h2>
            <form v-on:submit.prevent>
                <input type="text" v-model="newWho" placeholder="誰が">
                <button v-on:click="addWho">
                    Add Who
                </button>
                <input type="text" v-model="newWhen" placeholder="いつ">
                <button v-on:click="addWhen">
                    Add When
                </button>
                <input type="text" v-model="newWhere" placeholder="どこで">
                <button v-on:click="addWhere">
                    Add Where
                </button>
                <input type="text" v-model="newWhat" placeholder="なにを">
                <button v-on:click="addWhat">
                    Add What
                </button>
                <input type="text" v-model="newWhy" placeholder="なぜ">
                <button v-on:click="addWhy">
                    Add Why
                </button>
                <input type="text" v-model="newHow" placeholder="どのようにした">
                <button v-on:click="addHow">
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
      newWho: null,
      newWhen: null,
      newWhere: null,
      newWhat: null,
      newWhy: null,
      newHow: null,
      Who: {},
      When: {},
      Where: {},
      What: {},
      Why: {},
      How: {},
      errored: false,
      headers: {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*'
      }
    }
  },

  methods: {
    addWho: function () {
      if (this.newWho === '') return
      var who = this.newWho

      console.log(who)
      axios
        .post('http://localhost:8000/api/who', {'word': who}, this.headers)
        .then((response) => {
          console.log('OK', response)
        })
        .catch((err) => {
          console.log('word not found', err)
        })

      this.newWho = ''
    },

    addWhen: function () {
      if (this.newWhen === '') return
      var when = this.newWhen

      console.log(when)
      axios
        .post('http://localhost:8000/api/when', {'word': when}, this.headers)
        .then((response) => {
          console.log('OK', response)
        })
        .catch((err) => {
          console.log('word not found', err)
        })

      this.newWhen = ''
    },

    addWhere: function () {
      if (this.newWhere === '') return
      var where = this.newWhere

      console.log(where)
      axios
        .post('http://localhost:8000/api/where', {'word': where}, this.headers)
        .then((response) => {
          console.log('OK', response)
        })
        .catch((err) => {
          console.log('word not found', err)
        })

      this.newWhere = ''
    },

    addWhat: function () {
      if (this.newWhat === '') return
      var what = this.newWhat

      console.log(what)
      axios
        .post('http://localhost:8000/api/what', {'word': what}, this.headers)
        .then((response) => {
          console.log('OK', response)
        })
        .catch((err) => {
          console.log('word not found', err)
        })

      this.newWhat = ''
    },

    addWhy: function () {
      if (this.newWhy === '') return
      var why = this.newWhy

      console.log(why)
      axios
        .post('http://localhost:8000/api/why', {'word': why}, this.headers)
        .then((response) => {
          console.log('OK', response)
        })
        .catch((err) => {
          console.log('word not found', err)
        })

      this.newWhy = ''
    },

    addHow: function () {
      if (this.newHow === '') return
      var how = this.newHow

      console.log(how)
      axios
        .post('http://localhost:8000/api/how', {'word': how}, this.headers)
        .then((response) => {
          console.log('OK', response)
        })
        .catch((err) => {
          console.log('word not found', err)
        })

      this.newHow = ''
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
