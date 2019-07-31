<template>
  <b-card no-body>
    <element-table
      :endpoint="'users'"
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
      'email': 'E-mail',
      'first_name': 'Nome',
      'last_name': 'Sobrenome',
      'cell_phone': 'Telefone',
      'is_active': 'Ativo',
      'actions': 'Ações'
    }
  })
}
</script>

<style>

</style>
