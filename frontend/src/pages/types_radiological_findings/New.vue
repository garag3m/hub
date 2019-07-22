<template>
  <type-radiological-finding-form :type_radiological_finding="type_radiological_finding" @formSumit="create" />
</template>

<script>
import TypeRadiologicalFindingForm from './Form.vue'
export default {
  components: {
    TypeRadiologicalFindingForm
  },

  data: () => ({
    type_radiological_finding: {
      description_type: null,
      abbreviation: null,
      is_active: true
    }
  }),

  methods: {
    create (data) {
      this.$http.post('types-radiological-findings/', data)
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
            title: 'Erro no cadastro de Tipo de Cirurgia Mamária',
            message: 'Não foi possível cadastrar o Tipo de Cirurgia Mamária.'
          })
        })
    }
  }
}
</script>

<style>

</style>
