<template>
  <task-form :task="task" @formSumit="create" />
</template>

<script>
import TaskForm from './Form.vue'
export default {
  components: {
    TaskForm
  },

  data: () => ({
    task: {
        start_date: null,
        conclusion_date: null,
        title: null,
        about: null,
        // file: null
      }
  }),

  methods: {
    create (data) {
      this.$http.post('lattes/task/', data)
        .then((response) => {
          this.$router.push({ name: 'lattes/task-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro no cadastro do currículo',
            message: 'Não foi possível cadastrar o currículo.'
          })
        })
    }
  }
}
</script>

<style>

</style>
