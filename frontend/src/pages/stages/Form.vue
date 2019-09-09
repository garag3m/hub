<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="stage" :rules="rules" label-position="top" ref="stageForm">

      <el-form-item label="ALUNO:">
        <el-input v-model="stage.student" />
      </el-form-item>
      
      <el-form-item label="NOME DA EMPRESA:" prop="name">
        <el-input v-model="stage.company" />
      </el-form-item>

      <el-form-item label="ORIENTADOR:">
        <el-input v-model="stage.advisor"/>
      </el-form-item>

      <el-form-item label="SUPERVISOR:">
        <el-input v-model="stage.supervisor" />
      </el-form-item>
      
      <el-form-item label="SETOR:">
        <el-input v-model="stage.sector" />
      </el-form-item>

      <el-form-item label="DATA DE INÍCIO:" prop="start_date">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="stage.start_date" :bootstrap-styling="true" />
      </el-form-item>
      
      <el-form-item label="DATA FINAL:" prop="end_date">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="stage.end_date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="HORAS SEMANAIS:">
        <el-input type="number" :min="1" v-model="stage.week_hours" />
      </el-form-item>

      <el-form-item label="HORAS TOTAIS:">
        <el-input type="number" :min="1" v-model="stage.total_hours" />
      </el-form-item>

      <el-form-item label="DIAS SEMANAIS:">
        <el-input v-model="stage.days"/>
      </el-form-item>

      <el-form-item label="HORA DE INÍCIO:">
        <el-input v-model="stage.begins"/>
      </el-form-item>

      <el-form-item label="HORA FINAL:">
        <el-input v-model="stage.ends"/>
      </el-form-item>
      
      <el-form-item label="SEGURO:">
        <el-input v-model="stage.document_secure"/>
      </el-form-item>

      <el-form-item label="AUXÍLIO:">
        <el-radio-group v-model="stage.support">
          <el-radio-button label="S">Terá</el-radio-button>
          <el-radio-button label="N">Não terá</el-radio-button>
        </el-radio-group>
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
    Datepicker,
    ptBR
  },

props: {
    stage: {
      type: Object,
      default: () => ({
        student: null,
        company: null,
        advisor: null,
        supervisor: null,
        sector: null,
        start_date: null,
        end_date: null,
        week_hours: null,
        total_hours: null,
        days: null,
        begins: null,
        ends: null,
        document_secure: null,
        support: null 
      })
    }
  },
  data: () => ({
    companys_opts: [],
    students_opts: [],
    ptBR: ptBR,
    rules: {
     
    }     
  }),
  methods: {
    submit () {
      this.$refs['stageForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.stage)
        }
      })
    }
  },
  mounted () {
    this.$http.get('companys/')
      .then((response) => {
        this.companys_opts = response.data.results.map(item => {
          return { value: item.pk, text: item.name }
        })
      })
    this.$http.get('students/')
      .then((response) => {
        this.students_opts = response.data.results.map(item => {
          return { value: item.pk, text: item.name }
        })
      })
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
