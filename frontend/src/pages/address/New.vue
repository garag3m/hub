<template>
  <address-form :address="address" @formSumit="create" />
</template>

<script>
import AddressForm from './Form.vue'
export default {
  components: {
    AddressForm
  },

  data: () => ({
    address: {
      city: null,
      neighborhood: null,
      street: null,
      number: null,
      cep: null,
      state: null,
      country: null,
      name: null,
      type: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('address/', data)
        .then((response) => {
          this.$router.push({ name: 'address-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro de paciente',
            message: 'Não foi possível cadastrar o paciente.'
          })
        })
    }
  }
}
</script>

<style>

</style>
