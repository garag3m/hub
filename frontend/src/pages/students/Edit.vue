<template>
  <patient-form :patient="patient" @formSumit="update" />
</template>

<script>
import PatientForm from './Form.vue'
export default {
  components: {
    PatientForm
  },

  data: () => ({
    patient: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`patients/${data.id}/`, data)
        .then((response) => {
          this.$router.push({ name: 'patients-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no atualização de paciente',
            message: 'Não foi possível atualizar o paciente.'
          })
        })
    }
  },

  mounted () {
    const patientID = this.$route.params.id

    this.$http.get(`patients/${patientID}/`)
      .then((response) => {
        this.patient = response.data
      })
  }
}
</script>

<style>

</style>
