<template>
  <ct-form :ct="ct" @formSumit="update" />
</template>

<script>
import CtForm from './Form.vue'
export default {
  components: {
    CtForm
  },

  data: () => ({
    ct: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/ct/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/ct-list' })
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
    const ctID = this.$route.params.id

    this.$http.get(`lattes/ct/${ctID}/`)
      .then((response) => {
        this.ct = response.data
      })
  }
}
</script>

<style>

</style>
