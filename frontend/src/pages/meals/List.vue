<template>
  <b-card no-body>
    <element-table
      :endpoint="'meals'"
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
      'student_name': 'Aluno',
      'formated_date': 'Data',
      'type_name': 'Tipo',
      'presence': 'Presença',
    }
  })
}
</script>

<style>

</style>
