<template>
  <b-card no-body>
    <element-table
      :endpoint="'lattes/awards'"
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
      'year': 'Data',
      'award_name': 'Título do Prêmio',
      'actions': 'Ações'
    }
  })
}

</script>

<style>

</style>
