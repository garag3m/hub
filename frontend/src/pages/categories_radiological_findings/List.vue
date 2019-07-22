<template>
  <b-card no-body>
    <element-table
      :endpoint="'categories-radiological-findings'"
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
      'description_categorie': 'Descrição da Categoria de Achado Radiológico',
      'is_active': 'Ativo',
      'actions': 'Ações'
    }
  })
}
</script>

<style>

</style>
