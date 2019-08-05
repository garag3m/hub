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
      'student': 'Aluno',
      'date': 'Data',
      'type': 'Tipo'
    }
  })
}
</script>

<style>

</style>
