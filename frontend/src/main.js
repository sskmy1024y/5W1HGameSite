import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/ja'
import Vue from 'vue'

import App from './App'
import router from './router'


Vue.config.productionTip = false
Vue.use(ElementUI, {
  locale
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
