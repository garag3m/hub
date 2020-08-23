<template>
  <b-card no-body>
    <element-table
      :endpoint="'lattes/events'"
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
      'choice_choice': 'Meu Papel no Evento',
      'type_choice': 'Tipo de Evento',
      'name': 'Nome do Evento',
      'actions': 'Ações'
    }
  })
}

</script>

<style>

</style>
