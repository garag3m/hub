<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="request" :rules="rules" label-position="top" ref="requestForm">
      <h5>Dados do Pedido</h5>
      <el-form-item label="Lista de alunos" prop="student_list">
        <el-input v-model="request.student_list" />
      </el-form-item>

      <el-form-item label="Sexo do Paciente" prop="gender">
        <el-radio-group v-model="patient.gender">
          <el-radio-button label="1">Masculino</el-radio-button>
          <el-radio-button label="2">Feminino</el-radio-button>
        </el-radio-group>
      </el-form-item>

      <el-form-item label="Tipo">
        <b-select v-model="request.type" :options="type_opts" />
      </el-form-item>

      <el-form-item label="Data" prop="date">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="request.date" :bootstrap-styling="true" />
      </el-form-item>

      <el-form-item label="Cidade natal do Paciente">
        <el-input v-model="patient.naturalness"/>
      </el-form-item>

      <el-form-item label="País natal do Paciente">
        <el-input readonly value="Brasil" />
      </el-form-item>

      <el-form-item label="Escolaridade do Paciente">
        <b-form-select v-model="patient.schooling" :options="schooling_opts"></b-form-select>
      </el-form-item>

      <el-form-item label="Profissão do Paciente">
        <el-input v-model="patient.profession"/>
      </el-form-item>

      <br>
      <h5>Filiação</h5>
      <el-form-item label="Nome completo do pai">
        <el-input v-model="patient.father"/>
      </el-form-item>

      <el-form-item label="Nome completo da mãe">
        <el-input v-model="patient.mother"/>
      </el-form-item>

      <br>
      <h5>Documentação</h5>
      <el-form-item label="CPF" prop="cpf">
        <el-input v-mask="['###.###.###-##']" v-model="patient.cpf" />
      </el-form-item>

      <b-form-row>
        <el-form-item label="RG" class="col-md-6" prop="rg">
          <el-input v-mask="['##.###.###-##']" v-model="patient.rg" />
        </el-form-item>

        <el-form-item label="Entidade Emissora do RG" class="col-md-6">
          <el-input v-model="patient.rg_emitter"/>
        </el-form-item>
      </b-form-row>

      <el-form-item label="SUS">
        <el-input v-model="patient.sus"/>
      </el-form-item>

      <br>
      <h5>Contato</h5>
      <el-form-item label="Celular" prop="cell_phone">
        <el-input v-mask="['(##) #####-####']" v-model="patient.cell_phone" />
      </el-form-item>

      <el-form-item label="E-mail">
        <el-input v-model="patient.email"/>
      </el-form-item>

      <br>
      <h5>Endereço</h5>
      <el-form-item label="CEP" prop="cep">
        <el-input v-mask="['#####-###']" v-model="patient.cep" />
      </el-form-item>

      <el-form-item label="Endereço completo">
        <el-input v-model="patient.complete_address"/>
      </el-form-item>

      <el-form-item label="Número do endereço">
        <el-input v-model="patient.number_address"/>
      </el-form-item>

      <br>
      <h5>Responsável</h5>
      <el-form-item label="Responsável">
        <el-input v-model="patient.responsible_name"/>
      </el-form-item>

      <el-form-item label="Telefone do responsável" prop="responsible_cell_phone">
        <el-input v-mask="['(##)#####-####']" v-model="patient.responsible_cell_phone" />
      </el-form-item>

      <el-form-item label="Responsável pelo encaminhamento do Paciente">
        <el-input v-model="patient.forwarded_by"/>
      </el-form-item>

      <br>
      <h5>Anamnese</h5>
      <el-form-item label="Idade da primeira menstruação do Paciente">
        <el-input type="number" :min="1" v-model="patient.age_menstruation" />
      </el-form-item>

      <el-form-item label="Idade da primeira gestação do Paciente">
        <el-input type="number" :min="1" v-model="patient.age_gestation" />
      </el-form-item>

      <el-form-item label="Idade em que inicou a menopausa do Paciente">
        <el-input type="number" :min="1" v-model="patient.age_menopause" />
      </el-form-item>

      <el-form-item label="Observações">
        <b-form-textarea rows="4" v-model="patient.observation" />
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
    request: {
      type: Object,
      default: () => ({
        student_list: null,
        date: null,
        type: null,
        status: 1,
        justification_teacher: null,
        teacher: null,
      })
    }
  },

  data: () => ({
    rules: {
    },
    type_opts: [
      { value: 1, text: 'Almoço' },
      { value: 2, text: 'Jantar' },
    ],
  }),

  methods: {
    submit () {
      this.$refs['requestForm'].validate((valid) => {
        if (valid) {
          this.$emit('formSumit', this.patient)
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
