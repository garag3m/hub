<template>
  <b-card no-body>
    <element-table
      :endpoint="'files'"
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
      'user_name': 'Requerente',
      'status_name': 'Status',
      'file': 'Arquivo'
    }
  })
}
</script>

<style>

</style>
