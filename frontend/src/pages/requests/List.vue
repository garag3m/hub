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
      'date': 'Data',
      'type': 'Tipo',
      'status': 'Estado',
      'justification_teacher': 'Descrição',
      'teacher': 'Professor',
      'students': 'Alunos'
    }
  })
}
</script>

<style>

</style>
