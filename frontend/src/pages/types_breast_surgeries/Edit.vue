<template>
  <type-breast-surgery-form :type_breast_surgery="type_breast_surgery" @formSumit="update" />
</template>

<script>
import TypeBreastSurgeryForm from './Form.vue'
export default {
  components: {
    TypeBreastSurgeryForm
  },

  data: () => ({
    type_breast_surgery: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`types-breast-surgeries/${data.id}/`, data)
        .then((response) => {
          this.$router.push({ name: 'types-breast-surgeries-list' })
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
    const typesBreastSurgeriesID = this.$route.params.id

    this.$http.get(`types-breast-surgeries/${typesBreastSurgeriesID}/`)
      .then((response) => {
        this.type_breast_surgery = response.data
      })
  }
}
</script>

<style>

</style>
