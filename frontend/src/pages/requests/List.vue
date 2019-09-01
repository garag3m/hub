<template>
  <b-card no-body>
    <element-table
      :endpoint="'requests'"
      :columns="columns" /> 
  </b-card>
</template>

<script>
import ElementTable from '@/components/ElementTable.vue'

export default {
  components: {
    ElementTable
  },

  data: () => ({
    columns: {
      'students_amount': 'Alunos',
      'teacher_name': 'Professor',
      'formated_date': 'Data',
      'type_name': 'Tipo',
      'status_name': 'Status',
      'actions': 'Ações',
    }
  })
}
</script>

<style>

</style>
