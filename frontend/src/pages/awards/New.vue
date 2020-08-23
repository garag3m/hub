<template>
  <awards-form :awards="awards" @formSumit="create" />
</template>

<script>
import AwardsForm from './Form.vue'
export default {
  components: {
    AwardsForm
  },

  data: () => ({
    awards: {
        year: null,
        award_name: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/awards/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/awards-list' })
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
