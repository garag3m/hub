<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="location_radiological_finding" :rules="rules" ref="locationForm">
      <el-form-item label="Descrição Localização" prop="description_location">
        <el-input v-model="location_radiological_finding.description_location" />
      </el-form-item>

      <el-form-item label="Abreviação" prop="abbreviation">
        <el-input v-model="location_radiological_finding.abbreviation" />
      </el-form-item>

      <el-form-item>
        <div class="form-item">
          <label class="switcher switcher-success">
            <input type="checkbox" v-model="location_radiological_finding.location_radiological_finding" class="switcher-input" checked>
            <span class="switcher-indicator">
              <span class="switcher-yes"><span class="ion ion-md-checkmark"></span></span>
              <span class="switcher-no"><span class="ion ion-md-close"></span></span>
            </span>
            <span class="switcher-label">{{ location_radiological_finding.is_active ? "Ativo" : "Inativo" }}</span>
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
    location_radiological_finding: {
      type: Object,
      default: () => ({
        description_categorie: null,
        abbreviation: null,
        is_active: true
      })
    }
  },

  data: () => ({
    rules: {
      description_location: [
        { required: true, message: 'Informe a descrição', trigger: 'blur' },
        { max: 45, message: 'Tamanho da descrição deve ser menor ou igual à 45', trigger: 'blur' }
      ],
      abbreviation: [
        { required: true, message: 'Informe a abreviação', trigger: 'blur' },
        { max: 5, message: 'Tamanho da abreviação deve ser menor ou igual à 5', trigger: 'blur' }
      ]
    }
  }),

  methods: {
    submit () {
      this.$refs['locationForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.location_radiological_finding)
        }
      })
    }
  }
}
</script>
