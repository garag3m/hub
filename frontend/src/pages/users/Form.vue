<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="user" :rules="rules" label-position="top" ref="userForm">
      <h5>Dados do Usuário</h5>
      <el-form-item label="Username" prop="username">
        <div slot="label">Username</div>
        <el-input v-model="user.username" />
      </el-form-item>

      <el-form-item label="Nome" prop="first_name">
        <div slot="label">Nome</div>
        <el-input v-model="user.first_name" />
      </el-form-item>

      <el-form-item label="Sobrenome" prop="last_name">
        <div slot="label">Sobrenome</div>
        <el-input v-model="user.last_name" />
      </el-form-item>

      <el-form-item label="Email" prop="email">
        <div slot="label">Email</div>
        <el-input v-model="user.email" />
      </el-form-item>

      <el-form-item label="Senha" prop="password">
        <div slot="label">Senha</div>
        <el-input type="password" v-model="user.password" />
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
    user: {
      type: Object,
      default: () => ({
        username: null,
        first_name: null,
        last_name: null,
        email: null,
        password: null
      })
    }
  },

  data: () => ({
    rules: {
      username: [
        { required: true, message: 'Informe o nome', trigger: 'blur' }
      ],
    }
  }),

  methods: {
    submit () {
      this.$refs['userForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.user)
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
