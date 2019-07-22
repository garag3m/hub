<template>
  <categories-radiological-finding-form :category_radiological_finding="category_radiological_finding" @formSumit="update" />
</template>

<script>
import CategoriesRadiologicalFindingForm from './Form.vue'
export default {
  components: {
    CategoriesRadiologicalFindingForm
  },

  data: () => ({
    category_radiological_finding: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`categories-radiological-findings/${data.id}/`, data)
        .then((response) => {
          this.$router.push({ name: 'categories-radiological-findings-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          } else {
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no atualização de Categoria Achado Radiológio',
            message: 'Não foi possível atualizar o Categoria Achado Radiológio.'
          })
        })
    }
  },

  mounted () {
    const categoriesRadiologicalFindingID = this.$route.params.id

    this.$http.get(`categories-radiological-findings/${categoriesRadiologicalFindingID}/`)
      .then((response) => {
        this.category_radiological_finding = response.data
      })
  }
}
</script>

<style>

</style>
