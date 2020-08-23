<template>
  <languages-form :languages="languages" @formSumit="create" />
</template>

<script>
import LanguagesForm from './Form.vue'
export default {
  components: {
    LanguagesForm
  },

  data: () => ({
    languages: {
        language_name: null,
        reading_level: null,
        writing_level: null,
        speech_level: null,
        understanding_level: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/languages/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/languages-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro do currículo',
            message: 'Não foi possível cadastrar o currículo.'
          })
        })
    }
  }
}
</script>

<style>

</style>
