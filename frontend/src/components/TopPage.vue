<template>
  <div id="welcome">
    <section>
      <h1>5W1HGameSite</h1>
      {{ msg }}
    </section>
    <section>
      <router-link to="/Register">文章登録</router-link>
      <router-link to="/Generate">文章を生成</router-link>
    </section>
  </div>

</template>

<script>
export default {
  name: 'top_page',
  data () {
    return {
      msg: 'Hello'
    }
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
