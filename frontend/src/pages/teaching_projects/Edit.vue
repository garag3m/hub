<template>
  <teaching-projects-form :teaching_projects="teaching_projects" @formSumit="update" />
</template>

<script>
import TeachingProjectsForm from './Form.vue'
export default {
  components: {
    TeachingProjectsForm
  },

  data: () => ({
    teaching_projects: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/teaching-projects/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/teaching-projects-list' })
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
    const teaching_projectsID = this.$route.params.id

    this.$http.get(`lattes/teaching-projects/${teaching_projectsID}/`)
      .then((response) => {
        this.teaching_projects = response.data
      })
  }
}
</script>

<style>

</style>
