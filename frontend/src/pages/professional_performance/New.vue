<template>
  <professional-performance-form :professional_performance="professional_performance" @formSumit="create" />
</template>

<script>
import ProfessionalPerformanceForm from './Form.vue'
export default {
  components: {
    ProfessionalPerformanceForm
  },

  data: () => ({
    professional_performance: {
        start_date: null,
        conclusion_date: null,
        bond: null,
        occupation: null,
        workload: null,
        regime: null,
        tasks: null,
        institution: null,
        // file: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/professional-performance/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/professional-performance-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro do currículo',
            message: 'Não foi possível cadastrar o currículo.'
          })
        })
    }
  }
}
</script>

<style>

</style>
