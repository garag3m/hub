<template>
  <awards-form :awards="awards" @formSumit="update" />
</template>

<script>
import AwardsForm from './Form.vue'
export default {
  components: {
    AwardsForm
  },

  data: () => ({
    awards: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/awards/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/awards-list' })
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
    const awardsID = this.$route.params.id

    this.$http.get(`lattes/awards/${awardsID}/`)
      .then((response) => {
        this.awards = response.data
      })
  }
}
</script>

<style>

</style>
