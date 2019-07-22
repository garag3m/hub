<template>
  <user-form :user="user" @formSumit="create" />
</template>

<script>
import UserForm from './Form.vue'
export default {
  components: {
    UserForm
  },

  data: () => ({
    user: {
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
    create (data) {
      this.$http.post('users/', data)
        .then((response) => {
          this.$router.push({ name: 'users-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          } else {
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadatro de usuário',
            message: 'Não foi possível cadastrar o usuário.'
          })
        })
    }
  }
}
</script>

<style>

</style>
