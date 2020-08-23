<template>
  <occupation-area-form :occupation_area="occupation_area" @formSumit="create" />
</template>

<script>
import OccupationAreaForm from './Form.vue'
export default {
  components: {
    OccupationAreaForm
  },

  data: () => ({
    occupation_area: {
        area: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/occupation-area/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/occupation-area-list' })
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
