<template>
  <professional-performance-form :professional_performance="professional_performance" @formSumit="update" />
</template>

<script>
import ProfessionalPerformanceForm from './Form.vue'
export default {
  components: {
    ProfessionalPerformanceForm
  },

  data: () => ({
    professional_performance: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/professional-performance/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/professional-performance-list' })
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
    const professionalperformanceID = this.$route.params.id

    this.$http.get(`lattes/professional-performance/${professionalperformanceID}/`)
      .then((response) => {
        this.professional_performance = response.data
      })
  }
}
</script>

<style>

</style>
