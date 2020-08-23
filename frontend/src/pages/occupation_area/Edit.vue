<template>
  <occupation-area-form :occupation_area="occupation_area" @formSumit="update" />
</template>

<script>
import OccupationAreaForm from './Form.vue'
export default {
  components: {
    OccupationAreaForm
  },

  data: () => ({
    occupation_area: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/occupation-area/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/occupation-area-list' })
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
    const occupationareaID = this.$route.params.id

    this.$http.get(`lattes/occupation-area/${occupationareaID}/`)
      .then((response) => {
        this.occupation_area = response.data
      })
  }
}
</script>

<style>

</style>
