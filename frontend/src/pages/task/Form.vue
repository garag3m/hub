<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="task" :rules="rules" label-position="top" ref="taskForm">
      
      <h5>Cadastro de Instituição</h5>

      <el-form-item label="Data de Início">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="task.start_date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Data de Conclusão">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="task.conclusion_date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Titulo">
        <el-input v-model="task.title" />
      </el-form-item>

      <el-form-item label="Sobre">
        <el-input v-model="task.about" />
      </el-form-item>

      <!-- <el-form-item label="Arquivo">
        <el-input v-model="academic_education.file" />
      </el-form-item> -->

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
    task: {
      type: Object,
      default: () => ({
        start_date: null,
        conclusion_date: null,
        title: null,
        about: null,
        // file: null
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
      this.$refs['taskForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.task)
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
