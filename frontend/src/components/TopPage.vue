<template>
  <div id="welcome">
    <div class="head-line"></div>
    <section>
      <h1>5W1HGameSite</h1>
    </section>
    <section>
      <el-button type="primary" @click="$refs.registerDialog.dialog(true)">登録</el-button>
      <el-button type="danger">生成</el-button>
    </section>
    <Register ref="registerDialog" />
  </div>
</template>

<script>
import Register from './Register';
export default {
  name: 'top_page',
  data() {
    return {
      msg: 'Hello'
    };
  },
  components: {
    Register
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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

.head-line {
  background-color: red;
  width: 100%;
  height: 16px;
}
</style>
