<template>
  <b-card no-body>
    <element-table
      :endpoint="'students'"
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
      'registration': 'Matricula',
      'course': 'Curso',
      'status': 'Situação',
      'actions': 'Ações'
    }
  })
}
</script>

<style>

</style>
