<template>
  <complementary-education-form :complementary_education="complementary_education" @formSumit="update" />
</template>

<script>
import ComplementaryEducationForm from './Form.vue'
export default {
  components: {
    ComplementaryEducationForm
  },

  data: () => ({
    complementary_education: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/complementary-education/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/complementary-education-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização de Formação Complementar',
            message: 'Não foi possível atualizar a Formação Complementar.'
          })
        })
    }
  },

  mounted () {
    const complementaryeducationID = this.$route.params.id

    this.$http.get(`lattes/complementary-education/${complementaryeducationID}/`)
      .then((response) => {
        this.complementary_education = response.data
      })
  }
}
</script>

<style>

</style>
