<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="awards" :rules="rules" label-position="top" ref="awardsForm">
      
      <h5>Cadastro de Área de Atuação</h5>

      <el-form-item label="Data">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="awards.year" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Título do Prêmio">
        <el-input v-model="awards.award_name" />
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
    awards: {
      type: Object,
      default: () => ({
        year: null,
        award_name: null
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
      this.$refs['awardsForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.awards)
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
