<template>
  <breast-type-form :breast_type="breast_type" @formSumit="update" />
</template>

<script>
import BreastTypeForm from './Form.vue'
export default {
  components: {
    BreastTypeForm
  },

  data: () => ({
    breast_type: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`breast-types/${data.id}/`, data)
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
            title: 'Erro no atualização de Tipo de Mama',
            message: 'Não foi possível atualizar o Tipo de Mama.'
          })
        })
    }
  },

  mounted () {
    const breastTypeID = this.$route.params.id

    this.$http.get(`breast-types/${breastTypeID}/`)
      .then((response) => {
        this.breast_type = response.data
      })
  }
}
</script>

<style>

</style>
