<template>
  <type-breast-surgery-form :type_breast_surgery="type_breast_surgery" @formSumit="create" />
</template>

<script>
import TypeBreastSurgeryForm from './Form.vue'
export default {
  components: {
    TypeBreastSurgeryForm
  },

  data: () => ({
    type_breast_surgery: {
      description_surgery_type: null,
      is_active: true
    }
  }),

  methods: {
    create (data) {
      this.$http.post('types-breast-surgeries/', data)
        .then((response) => {
          this.$router.push({ name: 'types-breast-surgeries-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          } else {
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro de Tipo de Cirurgia Mamária',
            message: 'Não foi possível cadastrar o Tipo de Cirurgia Mamária.'
          })
        })
    }
  }
}
</script>

<style>

</style>
