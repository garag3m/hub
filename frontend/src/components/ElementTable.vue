<template>
  <div class="table-wrapper">
    <!-- Table controls -->
    <div class="row">
      <div class="col">
        <b-form-group>
          <b-select size="sm" :options="[10, 20, 40]" v-model="page.size" class="d-inline-block w-auto" />
          &nbsp; Por página
        </b-form-group>
      </div>
      <div class="col">
        <b-form-group>
          <b-input size="sm" placeholder="Buscar..." class="d-inline-block w-auto float-sm-right" />
        </b-form-group>
      </div>
    </div>
    <div class="table-responsive">

      <b-table
        responsive
        :fields="columns"
        :items="data">

        <template slot="is_active" slot-scope="scope">
          <i :class="`el-icon-${activeStatus(scope.item.is_active)}`" :style="`font-size: 30px; color: ${activeColor(scope.item.is_active)};`" />
        </template>

        <template slot="file" slot-scope="scope">
          <a :href="scope.item.file" target="_blank">
            <b-button variant="outline-primary" size="sm">Documento</b-button>
          </a>
        </template>

        <template slot="actions" slot-scope="scope">
          <router-link :to="{ name: `${endpoint}-edit`, params: { id: scope.item.pk } }">
            <b-button variant="outline-primary" size="sm">Editar</b-button>
          </router-link>

          <b-button variant="danger" size="sm" @click="displayDialog(scope.item.pk)">Remover</b-button>
        </template>

        <template slot="presence" slot-scope="scope">
          <b-button variant="success" size="sm" v-if="scope.item.attendance===null" @click="mealUpdate(scope.item.pk)">Conceder presença</b-button>
          <p v-else-if="scope.item.attendance===1">Presente</p>
          <p v-else-if="scope.item.attendance===2">Ausência</p>
        </template>
        
      </b-table>

    </div>
    <!-- Pagination -->
    <div class="row">
      <div class="col-sm">
        <router-link :to="{ name: `${endpoint}-new` }">
          <b-button variant="success">Novo registro</b-button>
        </router-link>
      </div>
      <div class="col-sm">
        <b-pagination class="justify-content-center justify-content-sm-end"
          v-if="page.size"
          v-model="page.number"
          :total-rows="90"
          :per-page="page.size" />
      </div>
    </div>

    <sweet-modal ref="remotionModal">
      <span>Tem certeza que deseja remover esse registro?</span>
      <b-btn slot="button" @click="$refs.remotionModal.close()">Não</b-btn>
      <b-btn slot="button" variant="primary" @click="deletion" class="ml-2">Sim</b-btn>
    </sweet-modal>
  </div>
</template>

<script>
import { SweetModal } from 'sweet-modal-vue'

export default {
  props: {
    endpoint: String,
    columns: {
      type: Object,
      default: () => {}
    }
  },

  components: {
    SweetModal
  },

  data: () => ({
    data: [],
    onLoading: false,
    dialogVisibility: null,
    dialogID: null,
    page: {
      total: null,
      number: 1,
      size: 10
    }
  }),

  methods: {
    requisition () {
      this.onLoading = true

      this.axios.get(`${this.endpoint}/`)
        .then((response) => {
          this.data = Object.values(response.data.results)
          this.onLoading = false
        })  
        .catch(() => {
          this.onLoading = false
        })
    },
    mealUpdate (id) {
      console.log(id)
      this.$http.patch(`meals/${id}/`, { attendance: 1 })
        .then((response) => {
          this.$router.push({ name: 'meals-list' })
        })
        .catch((error) => {
          if (error.response.status === 401) {
            localStorage.removeItem('jwt')
            this.$router.push({ name: 'login' })
          }
          this.$notify.error({
            title: 'Erro ao conceder presença',
            message: 'Não foi possível conceder presença.'
          })
        })
    },

    // RECORD DELETION =============================================
    displayDialog (id) {
      this.$refs.remotionModal.open()
      this.dialogID = id
    },

    hidesDialog () {
      this.$refs.remotionModal.close()
      this.dialogID = null
    },

    deletion () {
      this.axios.delete(`${this.endpoint}/${this.dialogID}/`)
        .then((response) => {
          this.$notify.success({
            title: 'Remoção feita com sucesso',
            message: 'Registro foi removido.'
          })

          this.requisition()
          this.hidesDialog()
        })
        .catch(() => {
          this.$notify.error({
            title: 'Não foi possivel realizar a remoção',
            message: 'Algo deu errado na hora de remover o registro.'
          })

          this.hidesDialog()
        })
    }
  },

  created () {
    this.requisition()
  }
}
</script>

<style>
.table-wrapper {
  padding: 1em;
}
</style>
