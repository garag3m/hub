<template>
  <institute-form :institute="institute" @formSumit="create" />
</template>

<script>
import InstituteForm from './Form.vue'
export default {
  components: {
    InstituteForm
  },

  data: () => ({
    institute: {
        name: null,
        url_homepage: null,
        address: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/institute/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/institute-list' })
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
