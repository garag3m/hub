<template>
  <events-form :events="events" @formSumit="update" />
</template>

<script>
import EventsForm from './Form.vue'
export default {
  components: {
    EventsForm
  },

  data: () => ({
    events: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/events/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/events-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização',
            message: 'Não foi possível atualizar'
          })
        })
    }
  },

  mounted () {
    const eventsID = this.$route.params.id

    this.$http.get(`lattes/events/${eventsID}/`)
      .then((response) => {
        this.events = response.data
      })
  }
}
</script>

<style>

</style>
