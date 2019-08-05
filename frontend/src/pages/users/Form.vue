<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form>
      <el-form-item>
        <div slot="label">Nome</div>
        <el-input v-model="user.first_name" />
      </el-form-item>

      <el-form-item>
        <div slot="label">Sobrenome</div>
        <el-input  v-model="user.last_name"/>
      </el-form-item>

      <el-form-item>
        <el-input  v-model="user.email"/>
        <div slot="label">E-mail</div>
      </el-form-item>

      <el-form-item>
        <div slot="label">CPF</div>
        <the-mask class="form-control" :mask="['###.###.###-##']" v-model="user.cpf" :masked="false" />
      </el-form-item>

      <el-form-item>
        <div slot="label">Telefone</div>
        <the-mask class="form-control" :mask="['(##) ####-####', '(##) #####-####']" v-model="user.cell_phone" :masked="false" />
      </el-form-item>

      <el-form-item>
        <div slot="label">Grupos</div>
        <b-form-select multiple v-model="user.groups" :options="group_opts"></b-form-select>
      </el-form-item>

      <el-form-item>
        <div slot="label">Senha</div>
        <el-input type="password" v-model="user.password"/>
      </el-form-item>

      <el-form-item>
        <div class="form-item">
          <label class="switcher switcher-success">
            <input type="checkbox" v-model="user.is_active" class="switcher-input" checked>
            <span class="switcher-indicator">
              <span class="switcher-yes"><span class="ion ion-md-checkmark"></span></span>
              <span class="switcher-no"><span class="ion ion-md-close"></span></span>
            </span>
            <span class="switcher-label">{{ user.is_active ? "Ativo" : "Inativo" }}</span>
          </label>
        </div>
      </el-form-item>

      <el-form-item>
        <b-btn variant="primary" @click="submit">Salvar</b-btn>
      </el-form-item>
    </el-form>
  </b-card>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      default: () => ({
        cpf: null,
        password: null,
        confirm_password: null,
        email: null,
        first_name: null,
        last_name: null,
        cell_phone: null,
        is_active: true,
        groups: null
      })
    }
  },

  data: () => ({
    group_opts: []
  }),

  methods: {
    submit () {
      this.$emit('formSumit', this.user)
    }
  },

  mounted () {
    this.$http.get('groups/')
      .then((response) => {
        this.group_opts = response.data.map((item) => {
          return { value: item.id, text: item.name }
        })
      })
  }
}
</script>

<style>

</style>
