<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="address" :rules="rules" label-position="top" ref="addressForm">
      
      <h5>Cadastro de Endereço</h5>

      <el-form-item label="Cidade">
        <div slot="label">Cidade</div>
        <el-input v-model="address.city"/>
      </el-form-item>

      <el-form-item label="Bairro">
        <div slot="label">Bairro</div>
        <el-input v-model="address.neighborhood"/>
      </el-form-item>

      <el-form-item label="Rua">
        <div slot="label">Rua</div>
        <el-input v-model="address.street"/>
      </el-form-item>

      <el-form-item label="Número">
        <div slot="label">Número</div>
        <el-input v-model="address.number"/>
      </el-form-item>

      <el-form-item label="Cep">
        <div slot="label">Cep</div>
        <el-input v-model="address.cep"/>
      </el-form-item>

      <el-form-item label="Estado">
        <div slot="label">Estado</div>
        <el-input v-model="address.state"/>
      </el-form-item>

      <el-form-item label="País">
        <div slot="label">País</div>
        <el-input v-model="address.country"/>
      </el-form-item>

      <el-form-item label="Nome">
        <div slot="label">Nome</div>
        <el-input v-model="address.name"/>
      </el-form-item>

      <el-form-item label="Tipo">
        <div slot="label">Tipo</div>
        <b-form-select v-model="address.type" :options="type_opts"></b-form-select>
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
    address: {
      type: Object,
      default: () => ({
        city: null,
        neighborhood: null,
        street: null,
        number: null,
        cep: null,
        state: null,
        country: null,
        name: null,
        type: null
      })
    }
  },

  data: () => ({
    rules: {
    },
    type_opts: [
      { value: 1, text: 'Profissional' },
      { value: 2, text: 'Residencial' },
      { value: 3, text: 'Outros' }
	],
}),

  methods: {

    submit () {
      this.$refs['addressForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.address)
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
