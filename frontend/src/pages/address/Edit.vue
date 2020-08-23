<template>
  <address-form :address="address" @formSumit="update" />
</template>

<script>
import AddressForm from './Form.vue'
export default {
  components: {
    AddressForm
  },

  data: () => ({
    address: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`address/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'address-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização do pedido',
            message: 'Não foi possível atualizar o pedido.'
          })
        })
    }
  },

  mounted () {
    const addressID = this.$route.params.id

    this.$http.get(`address/${addressID}/`)
      .then((response) => {
        this.address = response.data
      })
  }
}
</script>

<style>

</style>
