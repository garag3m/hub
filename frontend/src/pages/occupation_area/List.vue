<template>
  <b-card no-body>
    <element-table
      :endpoint="'lattes/occupation-area'"
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
      'area': 'Área de Atuação',
      'actions': 'Ações'
    }
  })
}

</script>

<style>

</style>
