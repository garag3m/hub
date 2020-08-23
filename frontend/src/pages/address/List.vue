<template>
  <b-card no-body>
    <element-table
      :endpoint="'address'"
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
      'city': 'Cidade',
      'street': 'Rua',
      'neighborhood': 'Bairro',
      'number': 'Número',
      'cep': 'CEP',
      'type': 'Tipo',
      'actions': 'Ações'
    }
  })
}
</script>

<style>

</style>
