<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="breast_type" :rules="rules" ref="breastForm">
      <el-form-item label="Descrição Tipo de Mama" prop="description_breast_type">
        <el-input v-model="breast_type.description_breast_type" />
      </el-form-item>

      <el-form-item>
        <div class="form-item">
          <label class="switcher switcher-success">
            <input type="checkbox" v-model="breast_type.is_active" class="switcher-input" checked>
            <span class="switcher-indicator">
              <span class="switcher-yes"><span class="ion ion-md-checkmark"></span></span>
              <span class="switcher-no"><span class="ion ion-md-close"></span></span>
            </span>
            <span class="switcher-label">{{ breast_type.is_active ? "Ativo" : "Inativo" }}</span>
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
    breast_type: {
      type: Object,
      default: () => ({
        description_breast_type: null,
        is_active: true
      })
    }
  },

  data: () => ({
    rules: {
      description_breast_type: [
        { required: true, message: 'Informe a descrição', trigger: 'blur' },
        { max: 45, message: 'Tamanho da descrição deve ser menor ou igual à 45', trigger: 'blur' }
      ]
    }
  }),

  methods: {
    submit () {
      this.$refs['breastForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.breast_type)
        }
      })
    }
  }
}
</script>

<style>

</style>
