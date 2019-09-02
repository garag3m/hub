<template>
  <request-form :request="request" @formSumit="update" />
</template>

<script>
import RequestForm from './FormEdit.vue'
export default {
  components: {
    RequestForm
  },

  data: () => ({
    request: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`requests/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'requests-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização do pedido',
            message: 'Não foi possível atualizar o pedido.'
          })
        })
    }
  },

  mounted () {
    const requestID = this.$route.params.id

    this.$http.get(`requests/${requestID}/`)
      .then((response) => {
        this.request = response.data
      })
  }
}
</script>

<style>

</style>
