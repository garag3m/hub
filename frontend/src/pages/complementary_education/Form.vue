<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="complementary_education" :rules="rules" label-position="top" ref="complementaryEducationForm">
      
      <h5>Cadastro de Instituição</h5>

      <el-form-item label="Data de Início">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="complementary_education.start_date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Data de Conclusão">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="complementary_education.conclusion_date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Nome da Graduação">
        <el-input v-model="complementary_education.graduation_level" />
      </el-form-item>

      <el-form-item label="Instituição">
        <b-form-select v-model="complementary_education.institution" :options="institution_opts"></b-form-select>
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
    complementary_education: {
      type: Object,
      default: () => ({
        start_date: null,
        conclusion_date: null,
        graduation_level: null,
        institution: null,
        // file: null
      })
    }
  },

  data: () => ({
    rules: {
    },
    institution_opts: [],
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['complementaryEducationForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.complementary_education)
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
