<template>
  <div id="welcome">
    <div class="head-line"></div>
    <section>
      <img :src="imgSrc" alt="title image" />
    </section>
    <section>
      <el-button type="primary" @click="$refs.registerDialog.dialog(true)">登録</el-button>
      <el-button type="danger" @click="$refs.generatorDialog.dialog(true)">生成</el-button>
    </section>
    <div class="foot-line">
      <div class="red"></div>
      <div class="blue"></div>
    </div>
    <Register ref="registerDialog" />
    <Generate ref="generatorDialog" />
  </div>
</template>

<script>
import TitleImage from '@/assets/title.png';
import Register from './Register';
import Generate from './Generate';
export default {
  name: 'top_page',
  data() {
    return {
      imgSrc: TitleImage,
      msg: 'Hello'
    };
  },
  components: {
    Register,
    Generate
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
  background-color: #e33e2a;
  width: 100%;
  height: 16px;
}

.foot-line {
  position: absolute;
  bottom: 0;
  width: 100%;
}

.foot-line .red {
  background-color: #e33e2a;
  height: 90px;
}

.foot-line .blue {
  background-color: #0d46a1;
  height: 16px;
}
</style>
