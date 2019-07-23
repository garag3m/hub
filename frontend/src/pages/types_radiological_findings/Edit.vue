<template>
  <type-radiological-finding-form :type_radiological_finding="type_radiological_finding" @formSumit="update" />
</template>

<script>
import TypeRadiologicalFindingForm from './Form.vue'
export default {
  components: {
    TypeRadiologicalFindingForm
  },

  data: () => ({
    type_radiological_finding: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`types-radiological-findings/${data.id}/`, data)
        .then((response) => {
          this.$router.push({ name: 'types-radiological-findings-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          } else {
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no atualização de Tipo de Cirurgia Mamária',
            message: 'Não foi possível atualizar o Tipo de Cirurgia Mamária.'
          })
        })
    }
  },

  mounted () {
    const typeRadiologicalFindingID = this.$route.params.id

    this.$http.get(`types-radiological-findings/${typeRadiologicalFindingID}/`)
      .then((response) => {
        this.type_radiological_finding = response.data
      })
  }
}
</script>

<style>

</style>
