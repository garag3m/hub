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
      'username': 'Nome de usuário',
      'first_name': 'Nome',
      'last_name': 'Sobrenome',
      'email': 'Email'
    }
  })
}
</script>

<style>

</style>
