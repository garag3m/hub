<template>
  <result-ultrasound-nodule-form :result_ultrasound_nodule="result_ultrasound_nodule" @formSumit="create" />
</template>

<script>
import ResultUltrasoundNoduleForm from './Form.vue'
export default {
  components: {
    ResultUltrasoundNoduleForm
  },

  data: () => ({
    result_ultrasound_nodule: {
      description_result_nodule: null,
      is_active: true
    }
  }),

  methods: {
    create (data) {
      this.$http.post('results-ultrasound-nodules/', data)
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
            title: 'Erro no cadastro de Resultado Nódulo Ultrassom',
            message: 'Não foi possível cadastrar o Resultado Nódulo Ultrassom.'
          })
        })
    }
  }
}
</script>

<style>

</style>
