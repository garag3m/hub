<template>
  <b-card no-body>
    <element-table
      :endpoint="'types-benign-findings'"
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
      'description_benign_type': 'Descrição Tipo de Achado Benigno',
      'is_active': 'Ativo',
      'actions': 'Ações'
    }
  })
}
</script>

<style>

</style>
