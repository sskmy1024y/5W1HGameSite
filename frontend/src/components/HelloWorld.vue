<template>
  <div id="welcome">
    <h1>5W1HGameSite</h1>

    <section v-if="errored">
      <p>Error</p>
    </section>

    <section v-else>
      <div class="axios_data">
        {{ info }}:
      </div>

    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'axios_data',
  data () {
    return {
      info: {},
      errored: false
    }
  },
  mounted () {
    const headers = {
      'Content-Type': 'application/json;charset=UTF-8',
      'Access-Control-Allow-Origin': '*'
      }
    axios
      .get('http://localhost:8000/api/all', {headers: headers})
      .then((response) => {
        this.info = response
        console.log('RESPONSE RECEIVED: ', response)
      })
      .catch((err) => {
        console.log('AXIOS ERROR: ', err)
        this.errored = true
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
