<template>
  <teaching-projects-form :teaching_projects="teaching_projects" @formSumit="create" />
</template>

<script>
import TeachingProjectsForm from './Form.vue'
export default {
  components: {
    TeachingProjectsForm
  },

  data: () => ({
    task: {
        start_date: null,
        conclusion_date: null,
        title: null,
        about: null,
        // file: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/teaching-projects/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/teaching-projects-list' })
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
