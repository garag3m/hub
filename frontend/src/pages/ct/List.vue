<template>
  <b-card no-body>
    <element-table
      :endpoint="'lattes/ct'"
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
      'title': 'Título',
      'actions': 'Ações'
    }
  })
}

</script>

<style>

</style>
