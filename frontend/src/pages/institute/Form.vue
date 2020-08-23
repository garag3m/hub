<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="institute" :rules="rules" label-position="top" ref="instituteForm">
      
      <h5>Cadastro de Instituição</h5>

      <el-form-item label="Nome da Instituição" prop="name">
        <el-input v-model="institute.name" />
      </el-form-item>

      <el-form-item label="URL da HOMEPAGE" prop="url_homepage">
        <el-input v-model="institute.url_homepage" />
      </el-form-item>

      <el-form-item label="Endereço" prop="institute.address">
        <b-form-select v-model="institute.address" :options="address_opts"></b-form-select>
      </el-form-item>

      <b-btn variant="primary" @click="submit">Salvar</b-btn>
    </el-form>
  </b-card>
</template>

<script>
import { ptBR } from 'vuejs-datepicker/dist/locale'
import moment from 'moment'

export default {
  components: {
  },

  props: {
    institute: {
      type: Object,
      default: () => ({
        name: null,
        url_homepage: null,
        address: null,
      })
    }
  },

  data: () => ({
    rules: {
    },
    address_opts: [],
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['instituteForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.institute)
        }
      })
    }
  },
  mounted () {
    this.$http.get('address/')
      .then((response) => {
        this.address_opts = response.data.results.map(item => {
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
