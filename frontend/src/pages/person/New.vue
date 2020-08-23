<template>
  <person-form :person="person" @formSumit="create" />
</template>

<script>
import personForm from './Form.vue'
export default {
  components: {
    personForm
  },

  data: () => ({
    person: {
        id_lattes: null,
        get_name: null,
        get_academic_education: null,
        get_complementary_education: null,
        get_professional_performance: null,
        get_teaching_projects: null,
        get_languages: null,
        get_award: null,
        get_productions: null,
        get_events: null,
        get_ct: null,
        other_informations: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/person/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/person-list' })
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
