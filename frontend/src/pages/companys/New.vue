<template>
  <company-form :company="company" @formSumit="create" />
</template>

<script>
import CompanyForm from './Form.vue'
export default {
  components: {
    CompanyForm
  },

  data: () => ({
    company: {
       name: null,
        cnpj: null,
        owner: null,
        agreement_number: null,
        cpf_owner: null,
        address:{
          city: null,
          neighborhood: null,
          street: null,
          number: null,
          cep: null,
          state: null
        }
    }
  }),

  methods: {
    create (data) {
      this.$http.post('companys/', data)
        .then((response) => {
          this.$router.push({ name: 'companys-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro da empresa',
            message: 'Não foi possível cadastrar a empresa.'
          })
        })
    }
  }
}
</script>

<style>

</style>
