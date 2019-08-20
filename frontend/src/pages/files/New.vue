<template>
  <patient-form :patient="patient" @formSumit="create" />
</template>

<script>
import PatientForm from './Form.vue'
export default {
  components: {
    PatientForm
  },

  data: () => ({
    patient: {
      name: null,
      gender: null,
      date_birth: null,
      address: null,
      color: null,
      civil_status: null,
      cpf: null,
      rg: null,
      rg_emitter: null,
      cns_sus: null,
      naturalness: null,
      nationality: null,
      mother: null,
      father: null,
      number_address: null,
      complete_address: null,
      cell_phone: null,
      whastapp: null,
      facebook: null,
      instagram: null,
      email: null,
      profession: null,
      responsible_name: null,
      responsible_cell_phone: null,
      schooling: null,
      forwarded_by: null,
      observation: null,
      age_menstruation: null,
      age_gestation: null,
      age_menopause: null,
      is_active: true
    }
  }),

  methods: {
    create (data) {
      this.$http.post('students/', data)
        .then((response) => {
          this.$router.push({ name: 'students-list' })
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
