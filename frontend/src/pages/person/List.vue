<template>
  <b-card no-body>
    <element-table
      :endpoint="'lattes/person'"
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
      'id_lattes': 'ID Lattes',
      'get_name': 'Nome de Usuário',
      'get_academic_education': 'Formação Acadêmica',
      'get_complementary_education': 'Formação Complementar',
      'get_professional_performance': 'Atuação Profissional',
      'get_teaching_projects': 'Projetos de Ensino',
      'get_languages': 'Idiomas',
      'get_award': 'Prêmios',
      'get_productions': 'Produções',
      'get_events': 'Eventos',
      'get_ct': 'CT',
      'other_informations': 'Outras Informações Relevantes',
      'actions': 'Ações'
    }
  })
}

</script>

<style>

</style>
