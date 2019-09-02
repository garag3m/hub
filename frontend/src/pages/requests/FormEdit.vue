<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="request" :rules="rules" label-position="top" ref="requestForm">
      <h5>Dados do Pedido</h5>
      
      <el-form-item label="Tipo">
        <b-select v-model="request.type" :options="type_opts" />
      </el-form-item>

      <el-form-item label="Status">
        <b-select v-model="request.status" :options="status_opts" />
      </el-form-item>

      <el-form-item label="Data" prop="date">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="request.date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Justificativa">
        <el-input v-model="request.justification_teacher"/>
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
    request: {
      type: Object,
      default: () => ({
        student_list: null,
        date: null,
        type: null,
        status: 1,
        justification_teacher: null,
        teacher: null,
      })
    }
  },

  data: () => ({
    rules: {
    },
    type_opts: [
      { value: 1, text: 'Almoço' },
      { value: 2, text: 'Jantar' },
    ],
    status_opts: [
      { value: 1, text: 'Em andamento' },
      { value: 2, text: 'Aprovado' },
      { value: 2, text: 'Reprovado' },
	],
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['requestForm'].validate((valid) => {
        if (valid) {
			this.request.date = moment(this.request.date).format('YYYY-MM-DD')
        	this.$emit('formSumit', this.request)
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
