<template>
  <b-card no-body>
    <element-table
      :endpoint="'lattes/productions'"
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
      'type_choice': 'Tipo de Produção',
      'header': 'Cabeçalho',
      'reference': 'Referência Bibliográfica',
      'actions': 'Ações'
    }
  })
}

</script>

<style>

</style>
