<template>
  <document-opinion-form :document_opinion="document_opinion" @formSumit="update" />
</template>

<script>
import DocumentOpinionForm from './Form.vue'
export default {
  components: {
    DocumentOpinionForm
  },

  data: () => ({
    document_opinion: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`document-opinions/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'document-opinions-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização do parecer',
            message: 'Não foi possível atualizar o parecer.'
          })
        })
    }
  },

  mounted () {
    const document_opinionID = this.$route.params.id

    this.$http.get(`document-opinions/${document_opinionID}/`)
      .then((response) => {
        this.document_opinion = response.data
      })
  }
}
</script>

<style>

</style>
