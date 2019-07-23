<template>
  <result-ultrasound-nodule-form :result_ultrasound_nodule="result_ultrasound_nodule" @formSumit="update" />
</template>

<script>
import ResultUltrasoundNoduleForm from './Form.vue'
export default {
  components: {
    ResultUltrasoundNoduleForm
  },

  data: () => ({
    result_ultrasound_nodule: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`results-ultrasound-nodules/${data.id}/`, data)
        .then((response) => {
          this.$router.push({ name: 'results-ultrasound-nodules-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          } else {
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no atualização de Resultado Nódulo Ultrassom',
            message: 'Não foi possível atualizar o Resultado Nódulo Ultrassom.'
          })
        })
    }
  },

  mounted () {
    const resultUltrasoundNoduleID = this.$route.params.id

    this.$http.get(`results-ultrasound-nodules/${resultUltrasoundNoduleID}/`)
      .then((response) => {
        this.result_ultrasound_nodule = response.data
      })
  }
}
</script>

<style>

</style>
