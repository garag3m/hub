<template>
  <productions-form :productions="productions" @formSumit="update" />
</template>

<script>
import ProductionsForm from './Form.vue'
export default {
  components: {
    ProductionsForm
  },

  data: () => ({
    productions: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/productions/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/productions-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização',
            message: 'Não foi possível atualizar'
          })
        })
    }
  },

  mounted () {
    const productionsID = this.$route.params.id

    this.$http.get(`lattes/productions/${productionsID}/`)
      .then((response) => {
        this.productions = response.data
      })
  }
}
</script>

<style>

</style>
