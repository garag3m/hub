<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="company" :rules="rules" label-position="top" ref="companyForm">
     
      <el-form-item label="NOME:" prop="name">
        <el-input v-model="company.name" />
      </el-form-item>
      <el-form-item label="CNPJ:">
        <el-input v-model="company.cnpj" />
      </el-form-item>
      <el-form-item label="CIDADE:">
        <el-input v-model="company.address.city" />
      </el-form-item>
      <el-form-item label="BAIRRO:">
        <el-input v-model="company.address.neighborhood"/>
      </el-form-item>
      <el-form-item label="RUA:">
        <el-input v-model="company.address.street"/>
      </el-form-item>
      <el-form-item label="NÚMERO:">
        <el-input v-model="company.address.number"/>
      </el-form-item>
      <el-form-item label="CEP:">
        <el-input v-model="company.address.cep"/>
      </el-form-item>
      <el-form-item label="ESTADO:">
        <el-input v-model="company.address.state"/>
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
        address: {
          city: null,
          neighborhood: null,
          street: null,
          number: null,
          cep: null,
          state: null
        }
        })
    }
  },

  data: () => ({
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
}
</script>

<style scoped>
h5 {
  color:grey;
}

</style>
