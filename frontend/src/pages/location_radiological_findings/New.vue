<template>
  <location-radiological-finding-form :location_radiological_finding="location_radiological_finding" @formSumit="create" />
</template>

<script>
import LocationRadiologicalFindingForm from './Form.vue'
export default {
  components: {
    LocationRadiologicalFindingForm
  },

  data: () => ({
    location_radiological_finding: {
      description_categorie: null,
      abbreviation: null,
      is_active: true
    }
  }),

  methods: {
    create (data) {
      this.$http.post('location-radiological-findings/', data)
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
            title: 'Erro no cadastro de Localização Achado',
            message: 'Não foi possível cadastrar o Localização Achado.'
          })
        })
    }
  }
}
</script>

<style>

</style>
