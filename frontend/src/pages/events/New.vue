<template>
  <events-form :events="events" @formSumit="create" />
</template>

<script>
import EventsForm from './Form.vue'
export default {
  components: {
    EventsForm
  },

  data: () => ({
    events: {
        type: null,
        header: null,
        reference: null,
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/events/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/events-list' })
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
