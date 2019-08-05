<template>
  <b-card no-body>
    <element-table
      :endpoint="'companys'"
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
      'name': 'Nome',
      'owner': 'Proprietário',
      'cnpj': 'CNPJ'
    }
  })
}
</script>

<style>

</style>
