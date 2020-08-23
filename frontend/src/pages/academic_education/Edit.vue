<template>
  <academic-education-form :academic_education="academic_education" @formSumit="update" />
</template>

<script>
import AcademicEducationForm from './Form.vue'
export default {
  components: {
    AcademicEducationForm
  },

  data: () => ({
    academic_education: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/academic-education/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/academic-education-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização de Formação Acadêmica/Titulação',
            message: 'Não foi possível atualizar a Formação Acadêmica/Titulação.'
          })
        })
    }
  },

  mounted () {
    const academiceducationID = this.$route.params.id

    this.$http.get(`lattes/academic-education/${academiceducationID}/`)
      .then((response) => {
        this.academic_education = response.data
      })
  }
}
</script>

<style>

</style>
