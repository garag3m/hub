<template>
  <breast-type-form :breast_type="breast_type" @formSumit="create" />
</template>

<script>
import BreastTypeForm from './Form.vue'
export default {
  components: {
    BreastTypeForm
  },

  data: () => ({
    breast_type: {
      description_breast_type: null,
      is_active: true
    }
  }),

  methods: {
    create (data) {
      this.$http.post('breast-types/', data)
        .then((response) => {
          this.$router.push({ name: 'breast-types-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          } else {
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro de Tipo de Mama',
            message: 'Não foi possível cadastrar o Tipo de Mama.'
          })
        })
    }
  }
}
</script>

<style>

</style>
