<template>
  <div class="generate-top">
    <section>
      <h1>生成</h1>
    </section>
    <section v-if="errored">
      <p>Error</p>
    </section>

    <section v-else>
      <div class="generate-sentence">
        {{ info.data.who.word}}
        {{ info.data.when.word}}
        {{ info.data.where.word}}
        {{ info.data.what.word}}
        {{ info.data.why.word}}
        {{ info.data.how.word}}
      </div>
      <div class="top-link">
        <router-link to="/">トップページに戻る</router-link>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'generate_sentence',
  data() {
    return {
      info: {},
      errored: false
    }
  },

  mounted() {
    const headers = {
      'Content-Type': 'application/json;charset=UTF-8',
      'Access-Control-Allow-Origin': '*'
    }

    axios
      .get('http://localhost:8000/api/all', headers)
      .then(response => {
        this.info = response
        console.log('RESPONSE RECEIVED: ', response)
      })
      .catch(err => {
        console.log('AXIOS ERROR: ', err)
        this.errored = true
      })
      .catch(err => {
        console.log('AXIOS ERROR: ', err)
        this.errored = true
      })
  }
}
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
