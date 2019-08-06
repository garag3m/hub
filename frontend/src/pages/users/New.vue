<template>
  <userform :user="user" @formSumit="create" />
</template>

<script>
import UserForm from './Form.vue'
export default {
  components: {
    UserForm
  },

  data: () => ({
    user: {
      username: null,
      first_name: null,
      last_name: null,
      email: null,
      password: null
      }
  }),

  methods: {
    create (data) {
      console.log('hey')
      console.log(data)
      this.$http.post('users/', data)
        .then((response) => {
          console.log(response)
          this.$router.push({ name: 'users-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro de paciente',
            message: 'Não foi possível cadastrar o paciente.'
          })
        })
    }
  }
}
</script>

<style>

</style>
