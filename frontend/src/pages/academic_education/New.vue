<template>
  <academic-education-form :academic_education="academic_education" @formSumit="create" />
</template>

<script>
import AcademicEducationForm from './Form.vue'
export default {
  components: {
    AcademicEducationForm
  },

  data: () => ({
    academic_education: {
        start_date: null,
        conclusion_date: null,
        graduation_level: null,
        graduation: null,
        institution: null,
        title: null,
        advisor: null,
        observations: null,
        // file: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/academic-education/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/academic-education-list' })
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
