<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="skin_type" :rules="rules" ref="skinForm">
      <el-form-item label="Descrição Tipo de Pele" prop="description_skin_type">
        <el-input v-model="skin_type.description_skin_type" />
      </el-form-item>

      <b-form-group>
        <div class="form-group">
          <label class="switcher switcher-success">
            <input type="checkbox" v-model="skin_type.is_active" class="switcher-input" checked>
            <span class="switcher-indicator">
              <span class="switcher-yes"><span class="ion ion-md-checkmark"></span></span>
              <span class="switcher-no"><span class="ion ion-md-close"></span></span>
            </span>
            <span class="switcher-label">{{ skin_type.is_active ? "Ativo" : "Inativo" }}</span>
          </label>
        </div>
      </b-form-group>

      <el-form-item>
        <b-btn variant="primary" @click="submit">Salvar</b-btn>
      </el-form-item>
    </el-form>
  </b-card>
</template>

<script>
export default {
  props: {
    skin_type: {
      type: Object,
      default: () => ({
        description_skin_type: null,
        is_active: true
      })
    }
  },

  data: () => ({
    rules: {
      description_skin_type: [
        { required: true, message: 'Informe a descrição', trigger: 'blur' },
        { max: 45, message: 'Tamanho da descrição deve ser menor ou igual à 45', trigger: 'blur' }
      ]
    }
  }),

  methods: {
    submit () {
      this.$refs['skinForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.skin_type)
        }
      })
    }
  }
}
</script>

<style>

</style>
