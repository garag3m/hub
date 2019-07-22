<template>
  <skin-type-form :skin_type="skin_type" @formSumit="update" />
</template>

<script>
import SkinTypeForm from './Form.vue'
export default {
  components: {
    SkinTypeForm
  },

  data: () => ({
    skin_type: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`skin-types/${data.id}/`, data)
        .then((response) => {
          this.$router.push({ name: 'skin-types-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          } else {
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no atualização de Tipo de Mama',
            message: 'Não foi possível atualizar o Tipo de Mama.'
          })
        })
    }
  },

  mounted () {
    const skinTypeID = this.$route.params.id

    this.$http.get(`skin-types/${skinTypeID}/`)
      .then((response) => {
        this.skin_type = response.data
      })
  }
}
</script>

<style>

</style>
