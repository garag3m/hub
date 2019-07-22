<template>
  <b-card no-body>
    <element-table
      :endpoint="'patients'"
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
      'is_active': 'Ativo',
      'actions': 'Ações'
    }
  })
}
</script>

<style>

</style>
