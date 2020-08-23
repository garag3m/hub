<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="ct" :rules="rules" label-position="top" ref="ctForm">
      
      <h5>Cadastro de CT</h5>

      <el-form-item label="Título">
        <el-input v-model="ct.title" />
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
    ct: {
      type: Object,
      default: () => ({
        title: null
      })
    }
  },

  data: () => ({
    rules: {
    },
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['ctForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.ct)
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
