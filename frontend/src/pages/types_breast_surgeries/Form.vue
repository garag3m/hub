<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="type_breast_surgery" :rules="rules" ref="typeForm">
      <el-form-item label="Descrição Tipo de Cirurgia Mamária" prop="description_surgery_type">
        <el-input v-model="type_breast_surgery.description_surgery_type" />
      </el-form-item>

      <el-form-item>
        <div class="form-item">
          <label class="switcher switcher-success">
            <input type="checkbox" v-model="type_breast_surgery.is_active" class="switcher-input" checked>
            <span class="switcher-indicator">
              <span class="switcher-yes"><span class="ion ion-md-checkmark"></span></span>
              <span class="switcher-no"><span class="ion ion-md-close"></span></span>
            </span>
            <span class="switcher-label">{{ type_breast_surgery.is_active ? "Ativo" : "Inativo" }}</span>
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
    type_breast_surgery: {
      type: Object,
      default: () => ({
        description_surgery_type: null,
        is_active: true
      })
    }
  },

  data: () => ({
    rules: {
      description_surgery_type: [
        { required: true, message: 'Informe a descrição', trigger: 'blur' },
        { max: 45, message: 'Tamanho da descrição deve ser menor ou igual à 45', trigger: 'blur' }
      ]
    }
  }),

  methods: {
    submit () {
      this.$refs['typeForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.type_breast_surgery)
        }
      })
    }
  }
}
</script>

<style>

</style>
