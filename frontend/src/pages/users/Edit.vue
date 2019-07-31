<template>
  <user-form :user="user" @formSumit="update" />
</template>

<script>
import UserForm from './Form.vue'
export default {
  components: {
    UserForm
  },

  data: () => ({
    user: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`users/${data.id}/`, data)
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
            title: 'Erro no atualização de usuário',
            message: 'Não foi possível atualizar o usuário.'
          })
        })
    }
  },

  mounted () {
    const userID = this.$route.params.id

    this.$http.get(`users/${userID}/`)
      .then((response) => {
        this.user = response.data
      })
  }
}
</script>

<style>

</style>
