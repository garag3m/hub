<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="category_radiological_finding" :rules="rules" ref="categoriesForm">
      <el-form-item label="Descrição da Categoria de Achado Radiológico" prop="description_categorie">
        <el-input v-model="category_radiological_finding.description_categorie" />
      </el-form-item>

      <el-form-item>
        <div class="form-item">
          <label class="switcher switcher-success">
            <input type="checkbox" v-model="category_radiological_finding.is_active" class="switcher-input" checked>
            <span class="switcher-indicator">
              <span class="switcher-yes"><span class="ion ion-md-checkmark"></span></span>
              <span class="switcher-no"><span class="ion ion-md-close"></span></span>
            </span>
            <span class="switcher-label">{{ category_radiological_finding.is_active ? "Ativo" : "Inativo" }}</span>
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
    category_radiological_finding: {
      type: Object,
      default: () => ({
        description_categorie: null,
        is_active: true
      })
    }
  },

  data: () => ({
    rules: {
      description_categorie: [
        { required: true, message: 'Informe a descrição', trigger: 'blur' },
        { max: 45, message: 'Tamanho da descrição deve ser menor ou igual à 45', trigger: 'blur' }
      ]
    }
  }),

  methods: {
    submit () {
      this.$refs['categoriesForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.category_radiological_finding)
        }
      })
    }
  }
}
</script>
