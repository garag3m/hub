import Vue from 'vue'
import App from './App'
import router from './router'

import BootstrapVue from 'bootstrap-vue'
import MaskedInput from 'vue-text-mask'
import Notifications from 'vue-notification'
import VueI18n from 'vue-i18n'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/pt-br'
import VueTheMask from 'vue-the-mask'
import VueAxios from 'vue-axios'
import axios from './backend/vue-axios/axios'

import globals from './globals'
import Popper from 'popper.js'

// Required to enable animations on dropdowns/tooltips/popovers
Popper.Defaults.modifiers.computeStyle.gpuAcceleration = false

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(Notifications)
Vue.use(ElementUI, { locale })
Vue.use(VueI18n)
Vue.component('masked-input', MaskedInput)
Vue.use(VueTheMask)
Vue.use(VueAxios, axios)

// Global RTL flag
Vue.mixin({
  data: globals
})

new Vue({
  router,
  axios,
  render: h => h(App)
}).$mount('#app')
