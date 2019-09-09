<template>
  <document-opinion-form :document_opinion="document_opinion" @formSumit="create" />
</template>

<script>
import DocumentOpinionForm from './Form.vue'
export default {
  components: {
    DocumentOpinionForm
  },

  data: () => ({
    document_opinion: {
      date: null,
      process_number: null,
      status: null,
      company: null,
    }
  }),

  methods: {
    create (data) {
      this.$http.post('document-opinions/', data)
        .then((response) => {
          this.$router.push({ name: 'document-opinions-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro parecer',
            message: 'Não foi possível cadastrar o parecer.'
          })
        })
    }
  }
}
</script>

<style>

</style>
