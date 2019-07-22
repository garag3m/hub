<template>
  <type-benign-finding-form :type_benign_finding="type_benign_finding" @formSumit="create" />
</template>

<script>
import TypeBenignFindingForm from './Form.vue'
export default {
  components: {
    TypeBenignFindingForm
  },

  data: () => ({
    type_benign_finding: {
      description_benign_type: null,
      is_active: true
    }
  }),

  methods: {
    create (data) {
      this.$http.post('types-benign-findings/', data)
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
            title: 'Erro no cadastro de Tipo de Achado Benigno',
            message: 'Não foi possível cadastrar o Tipo de Achado Benigno.'
          })
        })
    }
  }
}
</script>

<style>

</style>
