<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="academic_education" :rules="rules" label-position="top" ref="academicEducationForm">
      
      <h5>Cadastro de Titulação</h5>

      <el-form-item label="Data de Início">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="academic_education.start_date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Data de Conclusão">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="academic_education.conclusion_date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Nível de Graduação">
        <b-form-select v-model="academic_education.graduation_level" :options="graduation_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Nome da Graduação">
        <el-input v-model="academic_education.graduation" />
      </el-form-item>

      <el-form-item label="Instituição">
        <b-form-select v-model="academic_education.institution" :options="institution_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Título">
        <el-input v-model="academic_education.title" />
      </el-form-item>

      <el-form-item label="Orientador">
        <el-input v-model="academic_education.advisor" />
      </el-form-item>

      <el-form-item label="Observações">
        <el-input v-model="academic_education.observations" />
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
    academic_education: {
      type: Object,
      default: () => ({
        start_date: null,
        conclusion_date: null,
        graduation_level: null,
        graduation: null,
        institution: null,
        title: null,
        advisor: null,
        observations: null,
        // file: null
      })
    }
  },

  data: () => ({
    rules: {
    },
    graduation_opts: [
      { value: 0, text: 'Técnico'},
      { value: 1, text: 'Graduação'},
      { value: 2, text: 'Especialização'},
      { value: 3, text: 'Mestrado'},
      { value: 4, text: 'Doutorado'},
      { value: 5, text: 'Pós Doutorado'},
    ],
    institution_opts: [],
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['academicEducationForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.academic_education)
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
