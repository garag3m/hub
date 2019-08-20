<template>
  <b-card header-tag="h6" class="mb-4">
    <el-form @submit="submit" :model="patient" :rules="rules" label-position="top" ref="patientForm">
      <h5>Dados Pessoais do Paciente</h5>
      <el-form-item label="Nome completo" prop="name">
        <el-input v-model="patient.name" />
      </el-form-item>

      <el-form-item label="Sexo do Paciente" prop="gender">
        <el-radio-group v-model="patient.gender">
          <el-radio-button label="M">Masculino</el-radio-button>
          <el-radio-button label="F">Feminino</el-radio-button>
        </el-radio-group>
      </el-form-item>

      <el-form-item label="Estado Civil do Paciente">
        <b-select v-model="patient.civil_status" :options="civil_status_opts" />
      </el-form-item>

      <el-form-item label="Data de nascimento do Paciente" prop="date_birth">
        <datepicker :language="ptBR" format="dd/MM/yyyy" v-model="patient.date_birth" :bootstrap-styling="true" />
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

      <b-form-group>
        <div class="form-group">
          <label class="switcher switcher-success">
            <input type="checkbox" v-model="patient.is_active" class="switcher-input" checked>
            <span class="switcher-indicator">
              <span class="switcher-yes"><span class="ion ion-md-checkmark"></span></span>
              <span class="switcher-no"><span class="ion ion-md-close"></span></span>
            </span>
            <span class="switcher-label">{{ patient.is_active ? "Ativo" : "Inativo" }}</span>
          </label>
        </div>
      </b-form-group>

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
    patient: {
      type: Object,
      default: () => ({
        name: null,
        gender: null,
        date_birth: null,
        address: null,
        color: null,
        civil_status: null,
        cpf: null,
        rg: null,
        rg_emitter: null,
        cns_sus: null,
        naturalness: null,
        nationality: 'Brasil',
        mother: null,
        father: null,
        number_address: null,
        complete_address: null,
        cell_phone: null,
        whastapp: null,
        facebook: null,
        instagram: null,
        email: null,
        profession: null,
        responsible_name: null,
        responsible_cell_phone: null,
        schooling: null,
        forwarded_by: null,
        observation: null,
        age_menstruation: null,
        age_gestation: null,
        age_menopause: null,
        is_active: true
      })
    }
  },

  data: () => ({
    rules: {
      name: [
        { required: true, message: 'Informe o nome', trigger: 'blur' }
      ],
      gender: [
        { required: true, message: 'Informe o sexo do paciente', trigger: 'blur' }
      ],
      date_birth: [
        { required: true, message: 'Informe data de nascimento', trigger: 'blur' }
      ],
      cpf: [
        { required: true, message: 'Informe CPF', trigger: 'blur' },
        { min: 14, message: 'CPF deve possuir 14 caracteres', trigger: 'blur' }
      ],
      rg: [
        { min: 13, message: 'RG deve possuir 13 digitos', trigger: 'blur' }
      ],
      cell_phone: [
        { min: 14, message: 'Celular deve possuir 14 digitos', trigger: 'blur' }
      ],
      cep: [
        { min: 9, message: 'CEP deve possuir 9 digitos', trigger: 'blur' }
      ],
      responsible_cell_phone: [
        { min: 14, message: 'Telefone do responsável deve possuir 14 digitos', trigger: 'blur' }
      ]
    },
    schooling_opts: [],
    civil_status_opts: [
      { value: 'SO', text: 'Solteira(o)' },
      { value: 'CA', text: 'Casada(o)' },
      { value: 'SE', text: 'Separada(o)' },
      { value: 'DI', text: 'Divorciada(o)' },
      { value: 'VI', text: 'Viúva(o)' }
    ],
    ptBR: ptBR
  }),

  methods: {
    submit () {
      this.$refs['patientForm'].validate((valid) => {
        if (valid) {
          this.patient.date_birth = moment(this.patient.date_birth).format('YYYY-MM-DD')
          this.patient.cpf = this.patient.cpf ? this.patient.cpf.replace(/\D/g, '') : null
          this.patient.rg = this.patient.rg ? this.patient.rg.replace(/\D/g, '') : null
          this.patient.cell_phone = this.patient.cell_phone ? this.patient.cell_phone.replace(/\D/g, '') : null
          this.patient.cep = this.patient.cep ? this.patient.cep.replace(/\D/g, '') : null
          this.patient.responsible_cell_phone = this.patient.responsible_cell_phone ? this.patient.responsible_cell_phone.replace(/\D/g, '') : null

          this.$emit('formSumit', this.patient)
        }
      })
    }
  },

  mounted () {
    this.$http.get('schoolings/')
      .then((response) => {
        this.schooling_opts = response.data.map((item) => {
          return { value: item.id, text: item.name }
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
