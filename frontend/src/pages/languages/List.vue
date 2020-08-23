<template>
  <b-card no-body>
    <element-table
      :endpoint="'lattes/languages'"
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
      'get_language': 'Idioma',
      'reading_choice': 'Lê',
      'writing_choice': 'Escreve',
      'speech_choice': 'Fala',
      'understanding_choice': 'Entende',
      'actions': 'Ações'
    }
  })
}

</script>

<style>

</style>
