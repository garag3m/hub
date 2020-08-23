<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="languages" :rules="rules" label-position="top" ref="languagesForm">
      
      <h5>Cadastro de Área de Atuação</h5>

      <el-form-item label="Idioma">
        <b-form-select v-model="languages.language_name" :options="languages_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Eu leio...">
        <b-form-select v-model="languages.reading_level" :options="type_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Eu escrevo...">
        <b-form-select v-model="languages.writing_level" :options="type_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Eu falo...">
        <b-form-select v-model="languages.speech_level" :options="type_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Eu compreendo...">
        <b-form-select v-model="languages.understanding_level" :options="type_opts"></b-form-select>
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
    languages: {
      type: Object,
      default: () => ({
        language_name: null,
        reading_level: null,
        writing_level: null,
        speech_level: null,
        understanding_level: null
      })
    }
  },

  data: () => ({
    rules: {
    },
    type_opts: [
      { value: 0, text: 'Bem' },
      { value: 1, text: 'Razoavelmente' },
      { value: 2, text: 'Mal' }
  ],
  languages_opts: [
    { value: 0, text: 'Português' },
    { value: 1, text: 'Inglês' },
    { value: 2, text: 'Espanhol' },
    { value: 3, text: 'Francês' },
    { value: 4, text: 'Alemão' },
    { value: 5, text: 'Japonês' },
    { value: 6, text: 'Chinês' },
    { value: 7, text: 'Russo' },
    { value: 8, text: 'Turco' },
    { value: 9, text: 'Árabe' },
    { value: 10, text: 'Norueguês' }
  ],
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['languagesForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.languages)
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
