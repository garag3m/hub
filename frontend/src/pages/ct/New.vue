<template>
  <ct-form :ct="ct" @formSumit="create" />
</template>

<script>
import CtForm from './Form.vue'
export default {
  components: {
    CtForm
  },

  data: () => ({
    ct: {
        title: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/ct/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/ct-list' })
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
