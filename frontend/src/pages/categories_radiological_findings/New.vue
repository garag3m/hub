<template>
  <categories-radiological-finding-form :category_radiological_finding="category_radiological_finding" @formSumit="create" />
</template>

<script>
import CategoriesRadiologicalFindingForm from './Form.vue'
export default {
  components: {
    CategoriesRadiologicalFindingForm
  },

  data: () => ({
    category_radiological_finding: {
      description_categorie: null,
      is_active: true
    }
  }),

  methods: {
    create (data) {
      this.$http.post('categories-radiological-findings/', data)
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
            title: 'Erro no cadastro de Categoria Achado Radiológio',
            message: 'Não foi possível cadastrar o Categoria Achado Radiológio.'
          })
        })
    }
  }
}
</script>

<style>

</style>
