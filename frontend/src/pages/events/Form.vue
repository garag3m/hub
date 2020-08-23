<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="events" :rules="rules" label-position="top" ref="eventsForm">
      
      <h5>Cadastro de Produção</h5>

      <el-form-item label="Papel">
        <b-form-select v-model="events.choice" :options="choice_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Tipo de Evento">
        <b-form-select v-model="events.type" :options="type_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Nome do Evento">
        <el-input v-model="events.name"/>
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
    events: {
      type: Object,
      default: () => ({
        choice: null,
        type: null,
        name: null
      })
    }
  },

  data: () => ({
    rules: {
    },
    choice_opts: [
      { value: 0, text: 'Participei' },
      { value: 1, text: 'Organizei' },
    ],
    type_opts: [
      { value: 0, text: 'Evento' },
      { value: 1, text: 'Congresso' },
      { value: 2, text: 'Exposição' },
      { value: 3, text: 'Feira' }
    ],
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['eventsForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.events)
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
