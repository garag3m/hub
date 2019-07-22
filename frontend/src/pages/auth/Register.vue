<template>
  <div class="authentication-wrapper authentication-3">
    <div class="authentication-inner">

      <!-- Side container -->
      <!-- Do not display the container on extra small, small and medium screens -->
      <div class="d-none d-lg-flex col-lg-8 align-items-center ui-bg-cover ui-bg-overlay-container p-5" :style="`background-image: url('${baseUrl}img/login_image.jpg');`">
        <div class="ui-bg-overlay bg-dark opacity-50"></div>

        <!-- Text -->
        <div class="w-100 text-white px-5">
          <h1 class="display-2 font-weight-bolder mb-4">CRIE SUA<br>CONTA</h1>
          <div class="text-large font-weight-light">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vehicula ex eu gravida faucibus. Suspendisse viverra pharetra purus. Proin fringilla ac lorem at sagittis. Proin tincidunt dui et nunc ultricies dignissim.
          </div>
        </div>
        <!-- /.Text -->
      </div>
      <!-- / Side container -->

      <!-- Form container -->
      <div class="d-flex col-lg-4 align-items-center bg-white p-5">
        <!-- Inner container -->
        <!-- Have to add `.d-flex` to control width via `.col-*` classes -->
        <div class="d-flex col-sm-7 col-md-5 col-lg-12 px-0 px-xl-4 mx-auto">
          <div class="w-100">

            <!-- Form -->
            <form class="my-5" @submit="register">

              <b-form-group label="Nome">
                <b-input v-model="credentials.first_name" />
                <span class="span-error" v-show="validFirstName">
                  Informe nome
                </span>
              </b-form-group>

              <b-form-group label="Sobrenome">
                <b-input v-model="credentials.last_name" />
                <span class="span-error" v-show="validLastName">
                  Informe sobrenome
                </span>
              </b-form-group>

              <b-form-group label="CPF">
                <masked-input
                  class="form-control"
                  :mask="[/\d/, /\d/, /\d/, '.', /\d/, /\d/, /\d/, '.', /\d/, /\d/, /\d/, '-', /\d/, /\d/]"
                  v-model="credentials.cpf" />
                <span class="span-error" v-show="validCPF">
                  Informe CPF
                </span>
              </b-form-group>

              <b-form-group label="Email">
                <b-input v-model="credentials.email" />
                <span class="span-error" v-show="validEmail">
                  Informe e-mail
                </span>
              </b-form-group>

              <b-form-group label="Telefone">
                <masked-input
                  class="form-control"
                  :mask="['(', /\d/, /\d/, ')', ' ', /\d/, /\d/, /\d/, /\d/, /\d/, '.', /\d/, /\d/, /\d/, /\d/]"
                  v-model="credentials.cell_phone" />
                <span class="span-error" v-show="validCellphone">
                  Informe telefone
                </span>
              </b-form-group>

              <b-form-group label="Senha">
                <b-input type="password" v-model="credentials.password" />
              </b-form-group>

              <b-form-group label="Repita senha">
                <b-input type="password" v-model="credentials.confirm_password" />
                <span class="span-error" v-show="!isSamePassword">
                  Repita a senha informada no campo anterior
                </span>
              </b-form-group>

              <b-btn @click="register" variant="primary" :block="true" class="mt-4">Registrar-se</b-btn>
            </form>
            <!-- / Form -->

            <div class="text-center text-muted">
              Já possui conta cadastrada? <router-link :to="{ name: 'login'}">Efetuar login</router-link>
            </div>

          </div>
        </div>
      </div>
      <!-- / Form container -->

    </div>
  </div>
</template>

<!-- Page -->
<style src="@/vendor/styles/pages/authentication.scss" lang="scss"></style>

<script>
export default {
  name: 'register',
  metaInfo: {
    title: 'Cadastro'
  },

  data: () => ({
    credentials: {
      cpf: null,
      password: null,
      confirm_password: null,
      email: null,
      first_name: null,
      last_name: null,
      cell_phone: null,
      is_active: true
    }
  }),

  methods: {
    register () {
      this.$http.post('users/', this.credentials)
        .then((response) => {
          this.push({ name: 'login' })
        })
    }
  },

  computed: {
    validCPF () {
      return this.credentials.cpf === ''
    },
    validEmail () {
      return this.credentials.email === ''
    },
    validLastName () {
      return this.credentials.last_name === ''
    },
    validFirstName () {
      return this.credentials.first_name === ''
    },
    validCellphone () {
      return this.credentials.cell_phone === ''
    },
    isSamePassword () {
      return this.credentials.password === this.credentials.confirm_password
    }
  }
}
</script>
