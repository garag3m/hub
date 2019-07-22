<template>
  <skin-type-form :skin_type="skin_type" @formSumit="create" />
</template>

<script>
import SkinTypeForm from './Form.vue'
export default {
  components: {
    SkinTypeForm
  },

  data: () => ({
    skin_type: {
      description_skin_type: null,
      is_active: true
    }
  }),

  methods: {
    create (data) {
      this.$http.post('skin-types/', data)
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
            title: 'Erro no cadastro de Tipo de Mama',
            message: 'Não foi possível cadastrar o Tipo de Mama.'
          })
        })
    }
  }
}
</script>

<style>

</style>
