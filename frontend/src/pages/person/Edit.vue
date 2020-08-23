<template>
  <person-form :person="person" @formSumit="update" />
</template>

<script>
import PersonForm from './Form.vue'
export default {
  components: {
    PersonForm
  },

  data: () => ({
    person: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/person/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/person-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização de Instituição',
            message: 'Não foi possível atualizar a Instituição.'
          })
        })
    }
  },

  mounted () {
    const personID = this.$route.params.id

    this.$http.get(`lattes/person/${personID}/`)
      .then((response) => {
        this.person = response.data
      })
  }
}
</script>

<style>

</style>
