<template>
  <student-form :student="student" @formSumit="update" />
</template>

<script>
import StudentForm from './Form.vue'
export default {
  components: {
    StudentForm
  },

  data: () => ({
    student: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`students/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'students-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no atualização do Estudante',
            message: 'Não foi possível atualizar o Estudante.'
          })
        })
    }
  },

  mounted () {
    const studentID = this.$route.params.id

    this.$http.get(`students/${studentID}/`)
      .then((response) => {
        this.student = response.data
      })
  }
}
</script>

<style>

</style>
