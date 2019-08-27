<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="patient" :rules="rules" label-position="top" ref="patientForm">
      <h5>Dados da Refeição</h5>
    
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
    meal: {
      type: Object,
      default: () => ({
      })
    }
  },

  data: () => ({
    rules: {
    },
    ptBR: ptBR
  }),

  methods: {
    submit () {
      this.$refs['mealForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.meal)
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
