<template>
  <company-form :company="company" @formSumit="update" />
</template>

<script>
import CompanyForm from './Form.vue'
export default {
  components: {
    CompanyForm
  },

  data: () => ({
    company: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`companys/${data.id}/`, data)
        .then((response) => {
          this.$router.push({ name: 'companys-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização da empresa',
            message: 'Não foi possível atualizar a empresa.'
          })
        })
    }
  },

  mounted () {
    const companyID = this.$route.params.id

    this.$http.get(`companys/${companyID}/`)
      .then((response) => {
        this.comapny = response.data
      })
  }
}
</script>

<style>

</style>
