<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="student" :rules="rules" label-position="top" ref="studentForm">
      <h5>Dados do Estudantes</h5>
      <el-form-item label="Nome completo" prop="name">
        <el-input v-model="student.name" />
      </el-form-item>

      <el-form-item label="Curso" prop="course">
        <el-input v-model="student.course" />
      </el-form-item>

      <el-form-item label="Situação" prop="status">
        <el-input v-model="student.status" />
      </el-form-item>

      <el-form-item label="Matrícula" prop="registration">
        <el-input v-model="student.registration" />
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
    student: {
      type: Object,
      default: () => ({
        name: null,
        course: null,
        status: null,
        registration: null
      })
    }
  },

  data: () => ({
    rules: {
      name: [
        { required: true, message: 'Informe o nome', trigger: 'blur' }
      ],
    }
  }),

  methods: {
    submit () {
      this.$refs['studentForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.student)
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
