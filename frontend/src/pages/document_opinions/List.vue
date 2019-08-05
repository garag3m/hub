<template>
  <b-card no-body>
    <element-table
      :endpoint="'document-opinions'"
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
      'process_number': 'Nº de processo',
      'date': 'Data',
      'status': 'Status',
      'company': 'Empresa'
    }
  })
}
</script>

<style>

</style>
