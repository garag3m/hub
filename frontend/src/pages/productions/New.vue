<template>
  <productions-form :productions="productions" @formSumit="create" />
</template>

<script>
import ProductionsForm from './Form.vue'
export default {
  components: {
    ProductionsForm
  },

  data: () => ({
    productions: {
        type: null,
        header: null,
        reference: null,
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/productions/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/productions-list' })
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
