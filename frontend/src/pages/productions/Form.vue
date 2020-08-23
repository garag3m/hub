<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="productions" :rules="rules" label-position="top" ref="productionsForm">
      
      <h5>Cadastro de Produção</h5>

      <el-form-item label="Tipo de Produção">
        <b-form-select v-model="productions.type" :options="type_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Cabeçalho">
        <el-input v-model="productions.header"/>
      </el-form-item>

      <el-form-item label="Referência Bibliográfica">
        <el-input v-model="productions.reference"/>
      </el-form-item>

      <b-btn variant="primary" @click="submit">Salvar</b-btn>
    </el-form>
  </b-card>
</template>

<script>
import Datepicker from 'vuejs-datepicker'
import { ptBR } from 'vuejs-datepicker/dist/locale'
import moment from 'moment'

export default {
  components: {
    Datepicker
  },

  props: {
    productions: {
      type: Object,
      default: () => ({
        type: null,
        header: null,
        reference: null
      })
    }
  },

  data: () => ({
    rules: {
    },
    type_opts: [
      { value: 0, text: 'Produção Bibliográfica' },
      { value: 1, text: 'Produção Técnica' },
      { value: 2, text: 'Demais tipos de Produção' }
    ],
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['productionsForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.productions)
        }
      })
    }
  },
}
</script>

<style scoped>
h5 {
  color:grey;
}

.vdp-datepicker .input-group .form-control[readonly] {
  background: none !important;
}
</style>
