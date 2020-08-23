<template>
  <languages-form :languages="languages" @formSumit="update" />
</template>

<script>
import LanguagesForm from './Form.vue'
export default {
  components: {
    LanguagesForm
  },

  data: () => ({
    languages: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/languages/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/languages-list' })
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
    const languagesID = this.$route.params.id

    this.$http.get(`lattes/languages/${languagesID}/`)
      .then((response) => {
        this.languages = response.data
      })
  }
}
</script>

<style>

</style>
