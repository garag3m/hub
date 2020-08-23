<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="person" :rules="rules" label-position="top" ref="personForm">
      
      <h5>Cadastro de Curriculo</h5>

      <el-form-item label="ID Lattes">
        <el-input v-model="person.id_lattes"/>
      </el-form-item>

      <el-form-item label="Nome de Usuário">
        <el-input v-model="person.get_name"/>
      </el-form-item>

      <el-form-item label="Formação Acadêmica">
        <el-input v-model="person.get_academic_education"/>
      </el-form-item>

      <el-form-item label="Formação Complementar">
        <el-input v-model="person.get_complementary_education"/>
      </el-form-item>

      <el-form-item label="Atuação Profissional">
        <el-input v-model="person.get_professional_performance"/>
      </el-form-item>

      <el-form-item label="Projetos de Ensino">
        <el-input v-model="person.get_teaching_projects"/>
      </el-form-item>

      <el-form-item label="Idiomas">
        <el-input v-model="person.get_languages"/>
      </el-form-item>

      <el-form-item label="Prêmios">
        <el-input v-model="person.get_award"/>
      </el-form-item>
      
      <el-form-item label="Produções">
        <el-input v-model="person.get_productions"/>
      </el-form-item>

      <el-form-item label="Eventos">
        <el-input v-model="person.get_events"/>
      </el-form-item>

      <el-form-item label="CT">
        <el-input v-model="person.get_ct"/>
      </el-form-item>

      <el-form-item label="Outras Informações Relevantes">
        <el-input v-model="person.other_informations"/>
      </el-form-item>

      <!-- <el-form-item label="Endereço" prop="person.address">
        <b-form-select v-model="person.address" :options="address_opts"></b-form-select>
      </el-form-item> -->

      <b-btn variant="primary" @click="submit">Salvar</b-btn>
    </el-form>
  </b-card>
</template>

<script>
import { ptBR } from 'vuejs-datepicker/dist/locale'
import moment from 'moment'

export default {
  components: {
  },

  props: {
    person: {
      type: Object,
      default: () => ({
        id_lattes: null,
        get_name: null,
        get_academic_education: null,
        get_complementary_education: null,
        get_professional_performance: null,
        get_teaching_projects: null,
        get_languages: null,
        get_award: null,
        get_productions: null,
        get_events: null,
        get_ct: null,
        other_informations: null
      })
    }
  },

  data: () => ({
    rules: {
    },
    address_opts: [],
	ptBR: ptBR,
  }),

  methods: {
    submit () {
      this.$refs['personForm'].validate((valid) => {
        if (valid) {
        	this.$emit('formSumit', this.person)
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

.vdp-datepicker .input-group .form-control[readonly] {
  background: none !important;
}
</style>
