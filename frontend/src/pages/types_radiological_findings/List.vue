<template>
  <b-card no-body>
    <element-table
      :endpoint="'types-radiological-findings'"
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
      'description_type': 'Descrição Tipo Achado Radiológico',
      'abbreviation': 'Abreviação',
      'is_active': 'Ativo',
      'actions': 'Ações'
    }
  })
}
</script>

<style>

</style>
