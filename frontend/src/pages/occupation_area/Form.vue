<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="occupation_area" :rules="rules" label-position="top" ref="complementaryEducationForm">
      
      <h5>Cadastro de Área de Atuação</h5>

      <el-form-item label="Area de Atuação">
        <el-input v-model="occupation_area.area" />
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
    occupation_area: {
      type: Object,
      default: () => ({
        area: null
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
      this.$refs['occupationAreaForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.occupation_area)
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
