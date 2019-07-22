<template>
  <location-radiological-finding-form :location_radiological_finding="location_radiological_finding" @formSumit="update" />
</template>

<script>
import LocationRadiologicalFindingForm from './Form.vue'
export default {
  components: {
    LocationRadiologicalFindingForm
  },

  data: () => ({
    location_radiological_finding: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`location-radiological-findings/${data.id}/`, data)
        .then((response) => {
          this.$router.push({ name: 'location-radiological-findings-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          } else {
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no atualização de Localização Achado',
            message: 'Não foi possível atualizar o Localização Achado.'
          })
        })
    }
  },

  mounted () {
    const locationRadiologicalFindingID = this.$route.params.id

    this.$http.get(`location-radiological-findings/${locationRadiologicalFindingID}/`)
      .then((response) => {
        this.location_radiological_finding = response.data
      })
  }
}
</script>

<style>

</style>
