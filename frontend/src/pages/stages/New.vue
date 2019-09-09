<template>
  <stage-form :stage="stage" @formSumit="create" />
</template>

<script>
import StageForm from './Form.vue'
export default {
  components: {
    StageForm
  },

  data: () => ({
    stage: {
    }
  }),

  methods: {
    create (data) {
      this.$http.post('stages/', data)
        .then((response) => {
          this.$router.push({ name: 'stages-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro de estágio',
            message: 'Não foi possível cadastrar o estágio.'
          })
        })
    }
  }
}
</script>

<style>

</style>
