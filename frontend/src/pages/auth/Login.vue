<template>
  <div class="authentication-wrapper authentication-3">
    <div class="cui-example-inline-spacing">
      <notifications group="notifications-default" />
    </div>

    <div class="authentication-inner">

      <!-- Side container -->
      <!-- Do not display the container on extra small, small and medium screens -->
      <div class="d-none d-lg-flex col-lg-8 align-items-center ui-bg-cover ui-bg-overlay-container p-5" :style="`background-image: url('${baseUrl}img/logo_hub.png'); height: 49%; margin-top: 10% `">
      <!-- rgb(245, 123, 126) -->
      <!--<div class="ui-bg-overlay opacity-50" style="background-color: rgb(213, 213, 213)"></div>-->
      </div>
      <!-- / Side container -->

      <!-- Form container -->
      <div class="d-flex col-lg-4 align-items-center bg-white p-5">
        <!-- Inner container -->
        <!-- Have to add `.d-flex` to control width via `.col-*` classes -->
        <div class="d-flex col-sm-7 col-md-5 col-lg-12 px-0 px-xl-4 mx-auto">
          <div class="w-100">

            <!-- Logo -->
            <div class="d-flex justify-content-center align-items-center">
              <img :src="`${baseUrl}img/logoifpb.png`" height="120">
            </div>
            <!-- / Logo -->

           <!-- <h4 class="text-center text-lighter font-weight-normal mt-4 mb-0">Entre com sua conta</h4> -->

            <!-- Form -->
            <form class="my-4" @submit="login">
              <b-form-group label="Matrícula:">
                <the-mask class="form-control" :mask="['###########']" v-model="credentials.username" :masked="false" />
              </b-form-group>
              <b-form-group label="Senha:">
                <input class="form-control" type="password" v-model="credentials.password" />
              </b-form-group>

              <div class="d-flex justify-content-between align-items-center m-0">
                <b-check class="m-0">Manter-me conectado(a)</b-check>
                <b-btn variant="success" @click="login">Entrar</b-btn>
              </div>
            </form>
            <!-- / Form -->

          </div>
        </div>
      </div>
      <!-- / Form container -->

    </div>
    <loading
      :active.sync="isLoading"
      :can-cancel="false"
      :is-full-page="true" />
  </div>
</template>

<!-- Page -->
<style src="@/vendor/styles/pages/authentication.scss" lang="scss"></style>

<script>
// Import component
import Loading from 'vue-loading-overlay'
// Import stylesheet
import 'vue-loading-overlay/dist/vue-loading.css'
import { setTimeout } from 'timers';

export default {
  name: 'login-v3',
  components: {
    Loading
  },
  metaInfo: {
    title: 'Login'
  },

  data: () => ({
    credentials: {
      username: '',
      password: ''
    },
    isLoading: false
  }),

  methods: {
    login () {
      this.isLoading = true
      // API login request
      this.$http.post('auth/', { username: this.credentials.username, password: this.credentials.password })
        .then((response) => {
          console.log(response)
          localStorage.setItem('jwt', response.data.token)

          this.$router.replace(this.$route.query.redirect || '/')
        })
        .catch(() => {
          this.$notify.error({
            title: 'Erro ao logar',
            message: 'Não é possivel realizar o login com essas credenciais'
          })
        })
        .finally(() => {
          this.isLoading = false
        })
    }
  }
}
</script>
