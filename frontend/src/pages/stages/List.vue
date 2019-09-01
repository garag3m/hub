<template>
  <b-card no-body>
    <element-table
      :endpoint="'stages'"
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
      'advisor': 'Orientador',
      'supervisor': 'Supervisor',
      'sector': 'Setor'
    }
  })
}
</script>

<style>

</style>
