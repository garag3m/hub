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
      'company_name': 'Empresa', 
      'process_number': 'Nº de processo',
      'formated_date': 'Data',
      'status_name': 'Status',
      'actions': 'Ações',
    }
  })
}
</script>

<style>

</style>
