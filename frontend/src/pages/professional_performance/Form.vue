<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="professional_performance" :rules="rules" label-position="top" ref="professionalPerformanceForm">
      
      <h5>Cadastro de Instituição</h5>

      <el-form-item label="Instituição">
        <b-form-select v-model="professional_performance.institution" :options="institution_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Data de Início">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="professional_performance.start_date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Data de Conclusão">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="professional_performance.conclusion_date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Vínculo">
        <el-input v-model="professional_performance.bond" />
      </el-form-item>

      <el-form-item label="Ocupação">
        <el-input v-model="professional_performance.occupation" />
      </el-form-item>

      <el-form-item label="Carga Horaria">
        <el-input v-model="professional_performance.workload" />
      </el-form-item>

      <el-form-item label="Regime">
        <el-input v-model="professional_performance.regime" />
      </el-form-item>

      <el-form-item label="Atividades">
        <b-form-select v-model="professional_performance.task" :options="task_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Area de Atuação">
        <el-input v-model="professional_performance.occupation_area" />
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
    professional_performance: {
      type: Object,
      default: () => ({
        start_date: null,
        conclusion_date: null,
        bond: null,
        occupation: null,
        workload: null,
        regime: null,
        tasks: null,
        institution: null,
        occupation_area: null
        // file: null
      })
    }
  },

  data: () => ({
    rules: {
    },
    institution_opts: [],
    task_opts: [],
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['professionalPerformanceForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.professional_performance)
        }
      })
    }
  },
  mounted () {
    this.$http.get('lattes/institute/')
      .then((response) => {
        this.institution_opts = response.data.results.map(item => {
          return { value: item.pk, text: item.name }
        })
      })
//     this.$http.get('lattes/task/')
//       .then((response) => {
//         this.task_opts = response.data.results.map(item => {
//           return { value: item.pk, text: item.name }
//       })
//     })
  }
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
