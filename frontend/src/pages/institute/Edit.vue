<template>
  <institute-form :institute="institute" @formSumit="update" />
</template>

<script>
import InstituteForm from './Form.vue'
export default {
  components: {
    InstituteForm
  },

  data: () => ({
    institute: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/institute/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/institute-list' })
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
    const instituteID = this.$route.params.id

    this.$http.get(`lattes/institute/${instituteID}/`)
      .then((response) => {
        this.institute = response.data
      })
  }
}
</script>

<style>

</style>
