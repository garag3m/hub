<template>
  <student-form :student="student" @formSumit="create" />
</template>

<script>
import StudentForm from './Form.vue'
export default {
  components: {
    StudentForm
  },

  data: () => ({
    student: {
      name: null,
      course: null,
      status: null,
      registration: null
    }
  }),

  methods: {
    create (data) {
      console.log('hey')
      console.log(data)
      this.$http.post('students/', data)
        .then((response) => {
          console.log(response)
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
