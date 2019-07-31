<template>
  <b-card no-body>
    <element-table
      :endpoint="'types-breast-surgeries'"
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
      'description_surgery_type': 'Descrição Tipo de Cirurgia Mamária',
      'is_active': 'Ativo',
      'actions': 'Ações'
    }
  })
}
</script>

<style>

</style>
