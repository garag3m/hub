<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="result_ultrasound_nodule" :rules="rules" ref="resultForm">
      <el-form-item label="Descrição Tipo de Pele" prop="description_result_nodule">
        <el-input v-model="result_ultrasound_nodule.description_result_nodule" />
      </el-form-item>

      <el-form-item>
        <div class="form-item">
          <label class="switcher switcher-success">
            <input type="checkbox" v-model="result_ultrasound_nodule.is_active" class="switcher-input" checked>
            <span class="switcher-indicator">
              <span class="switcher-yes"><span class="ion ion-md-checkmark"></span></span>
              <span class="switcher-no"><span class="ion ion-md-close"></span></span>
            </span>
            <span class="switcher-label">{{ result_ultrasound_nodule.is_active ? "Ativo" : "Inativo" }}</span>
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
    result_ultrasound_nodule: {
      type: Object,
      default: () => ({
        description_result_nodule: null,
        is_active: true
      })
    }
  },

  data: () => ({
    rules: {
      description_result_nodule: [
        { required: true, message: 'Informe a descrição', trigger: 'blur' },
        { max: 45, message: 'Tamanho da descrição deve ser menor ou igual à 45', trigger: 'blur' }
      ]
    }
  }),

  methods: {
    submit () {
      this.$refs['resultForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.result_ultrasound_nodule)
        }
      })
    }
  }
}
</script>

<style>

</style>
