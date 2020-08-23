<template>
  <b-card no-body>
    <element-table
      :endpoint="'lattes/academic-education'"
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
      'start_date': 'Data de Início',
      'get_conclusion_date': 'Data de Conclusão',
      'graduation_choice': 'Nível',
      'graduation': 'Graduação',
      'get_institution': 'Instituição',
      'actions': 'Ações'
    }
  })
}

</script>

<style>

</style>
