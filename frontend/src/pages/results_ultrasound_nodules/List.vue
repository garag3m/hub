<template>
  <b-card no-body>
    <element-table
      :endpoint="'skin-types'"
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
      'description_skin_type': 'Descrição Tipo de Pele',
      'is_active': 'Ativo',
      'actions': 'Ações'
    }
  })
}
</script>

<style>

</style>
