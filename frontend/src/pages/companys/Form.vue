<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="company" :rules="rules" label-position="top" ref="companyForm">
     
      <el-form-item label="NOME:" prop="name">
        <el-input v-model="company.name" />
      </el-form-item>

      <el-form-item label="CNPJ:">
        <el-input v-model="company.cnpj" />
      </el-form-item>

      <el-form-item label="ENDEREÇO" prop="address">
        <b-form-select v-model="company.address" :options="address_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="PROPRIETÁRIO:">
        <el-input v-model="company.owner" />
      </el-form-item>

      <el-form-item label="NÚMERO DO CONVENIO:">
        <el-input type="number" :min="1" v-model="company.agreement_number" />
      </el-form-item>

      <el-form-item label="CPF DO PROPRIETÁRIO::">
        <el-input v-model="company.cpf_owner" />
      </el-form-item>

      <b-btn variant="primary" @click="submit">Salvar</b-btn>
    </el-form>
  </b-card>
</template>

<script>

export default {
  components: {
    
  },

  props: {
    company: {
      type: Object,
      default: () => ({
        name: null,
        cnpj: null,
        owner: null,
        agreement_number: null,
        cpf_owner: null,
        address: null
      })
    }
  },

  data: () => ({
    address_opts: [],
  }),

  methods: {

    submit () {
      this.$refs['companyForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.company)
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

</style>
