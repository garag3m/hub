<template>
  <request-form :request="request" @formSumit="create" />
</template>

<script>
import RequestForm from './Form.vue'
export default {
  components: {
    RequestForm
  },

  data: () => ({
    request: {
        student_list: null,
        date: null,
        type: null,
        status: 1,
        justification_teacher: null,
        teacher: null,
      }
  }),

  methods: {
    create (data) {
      this.$http.post('requests/', data)
        .then((response) => {
          this.$router.push({ name: 'requests-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro do pedido',
            message: 'Não foi possível cadastrar o pedido.'
          })
        })
    }
  }
}
</script>

<style>

</style>
