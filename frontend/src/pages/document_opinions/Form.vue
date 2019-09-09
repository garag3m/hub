<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="document_opinion" :rules="rules" label-position="top" ref="documentOpinionForm"> 

      <el-form-item label="Data:" prop="date">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="document_opinion.date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Numero do processo:">
        <el-input type="number" :min="1" v-model="document_opinion.process_number" />
      </el-form-item>

      <el-form-item label="Status:" prop="status">
        <el-radio-group v-model="document_opinion.status">
          <el-radio-button label="1">Deferido</el-radio-button>
          <el-radio-button label="2">Indeferido</el-radio-button>
        </el-radio-group>
      </el-form-item>

      <el-form-item label="Empresa">
        <b-form-select v-model="document_opinion.company" :options="companys_opts"></b-form-select>
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
    document_opinion: {
      type: Object,
      default: () => ({
        date: null,
        process_number: null,
        status: null,
        company: null,
      })
    }
  },

  data: () => ({
    companys_opts: [],
    ptBR: ptBR
  }),
  methods: {

    submit () {
      this.$refs['documentOpinionForm'].validate((valid) => {
        if (valid) {
          this.document_opinion.date = moment(this.document_opinion.date).format('YYYY-MM-DD')
          this.$emit('formSumit', this.document_opinion)
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
