<template>
  <task-form :task="task" @formSumit="update" />
</template>

<script>
import TaskForm from './Form.vue'
export default {
  components: {
    TaskForm
  },

  data: () => ({
    task: {}
  }),

  methods: {
    update (data) {
      this.$http.put(`lattes/task/${data.pk}/`, data)
        .then((response) => {
          this.$router.push({ name: 'lattes/task-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro na atualização de Formação Complementar',
            message: 'Não foi possível atualizar a Formação Complementar.'
          })
        })
    }
  },

  mounted () {
    const taskID = this.$route.params.id

    this.$http.get(`lattes/task/${taskID}/`)
      .then((response) => {
        this.task = response.data
      })
  }
}
</script>

<style>

</style>
