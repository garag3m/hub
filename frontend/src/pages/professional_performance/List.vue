<template>
  <b-card no-body>
    <element-table
      :endpoint="'lattes/professional-performance'"
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
      'start_date': 'Data de Inicio',
      'get_conclusion_date': 'Data de Conclusao',
      'bond': 'Vinculo',
      'occupation': 'Ocupação',
      'workload': 'Carga Horaria',
      'regime': 'Regime',
      'tasks_list': 'Atividades',
      'get_institution': 'Instituição',
      'occupation_area': 'Área de Atuação',
      'actions': 'Ações'
    }
  })
}

</script>

<style>

</style>
