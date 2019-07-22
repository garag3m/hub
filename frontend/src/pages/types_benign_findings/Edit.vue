<template>
  <type-benign-finding-form :type_benign_finding="type_benign_finding" @formSumit="update" />
</template>

<script>
import TypeBenignFindingForm from './Form.vue'
export default {
  components: {
    TypeBenignFindingForm
  },

  data: () => ({
    type_benign_finding: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`types-benign-findings/${data.id}/`, data)
        .then((response) => {
          this.$router.push({ name: 'types-benign-findings-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          } else {
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no atualização de Tipo de Achado Benigno',
            message: 'Não foi possível atualizar o Tipo de Achado Benigno.'
          })
        })
    }
  },

  mounted () {
    const typeBenignFindingID = this.$route.params.id

    this.$http.get(`types-benign-findings/${typeBenignFindingID}/`)
      .then((response) => {
        this.type_benign_finding = response.data
      })
  }
}
</script>

<style>

</style>
