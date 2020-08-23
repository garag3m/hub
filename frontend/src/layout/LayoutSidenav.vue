<template>
  <sidenav :orientation="orientation" class="sidenav sidenav-vertical layout-sidenav bg-white">
    <!-- Brand demo (see src/demo.css) -->
    <div class="app-brand demo" v-if="orientation !== 'horizontal'">
      <router-link to="/" class="app-brand-text demo sidenav-text font-weight-normal ml-2">
        <span class="app-brand-logo">
          <img :src="`${baseUrl}img/logo_hub.png`" height="36">
        </span>
      </router-link>

      <a href="javascript:void(0)" class="layout-sidenav-toggle sidenav-link text-large ml-auto" @click="toggleSidenav()">
        <i class="ion ion-md-menu align-middle"></i>
      </a>
    </div>
    <div class="sidenav-divider mt-0" v-if="orientation !== 'horizontal'"></div>

    <!-- Inner -->
    <div class="sidenav-inner" :class="{ 'py-1': orientation !== 'horizontal' }">
    <sidenav-router-link icon="ion ion-md-home" to="/" :exact="true">Home</sidenav-router-link>

      <sidenav-menu icon="ion ion-md-people" :active="isMenuActive('/aux')" :open="isMenuOpen('/aux')">
      <template slot="link-text">CORE</template>
        <sidenav-router-link icon="ion ion-md-people" :to="{ name: 'users-list' }" :exact="true">Usuários</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-leaf" :to="{ name: 'address-list' }" :exact="true">Endereços</sidenav-router-link>
      </sidenav-menu>

      <sidenav-menu icon="ion ion-ios-school" :active="isMenuActive('/aux')" :open="isMenuOpen('/aux')">
        <template slot="link-text">EDU</template>
        <sidenav-router-link icon="ion ion-md-person" :to="{ name: 'students-list' }" :exact="true">Alunos</sidenav-router-link>
      </sidenav-menu>

      <sidenav-menu icon="ion ion-md-pizza" :active="isMenuActive('/aux')" :open="isMenuOpen('/aux')">
        <template slot="link-text">IFOOD</template>
        <sidenav-router-link icon="ion ion-md-paper" :to="{ name: 'requests-list' }" :exact="true">Pedidos</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-restaurant" :to="{ name: 'meals-list' }" :exact="true">Refeição</sidenav-router-link>
      </sidenav-menu>

      <sidenav-menu icon="ion ion-ios-document" :active="isMenuActive('/aux')" :open="isMenuOpen('/aux')">
        <template slot="link-text">CERE</template>
        <sidenav-router-link icon="ion ion-md-clipboard" :to="{ name: 'companys-list' }" :exact="true">Empresas</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-briefcase" :to="{ name: 'stages-list' }" :exact="true">Estágios</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-contacts" :to="{ name: 'document-opinions-list' }" :exact="true">Pareceres</sidenav-router-link>
      </sidenav-menu>

      <sidenav-menu icon="ion ion-ios-print" :active="isMenuActive('/aux')" :open="isMenuOpen('/aux')">
        <template slot="link-text">CTRL_P</template>
        <sidenav-router-link icon="ion ion-md-document" :to="{ name: 'files-list' }" :exact="true">Documento</sidenav-router-link>
      </sidenav-menu>

      <sidenav-menu icon="ion ion-md-attach" :active="isMenuActive('/aux')" :open="isMenuOpen('/aux')">
        
        <template slot="link-text">LATTES</template>

        <sidenav-router-link icon="ion ion-md-finger-print" :to="{ name: 'lattes/person-list' }" :exact="true">Currículos</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-home" :to="{ name: 'lattes/institute-list' }" :exact="true">Instituições</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-book" :to="{ name: 'lattes/academic-education-list' }" :exact="true">Formação Acadêmica/Titulação</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-book" :to="{ name: 'lattes/complementary-education-list' }" :exact="true">Formação Complementar</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-paper" :to="{ name: 'lattes/task-list' }" :exact="true">Atividades</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-man" :to="{ name: 'lattes/professional-performance-list' }" :exact="true">Atuação Profissional</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-hand" :to="{ name: 'lattes/teaching-projects-list' }" :exact="true">Projetos de Ensino</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-planet" :to="{ name: 'lattes/languages-list' }" :exact="true">Languages</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-trophy" :to="{ name: 'lattes/awards-list' }" :exact="true">Awards</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-create" :to="{ name: 'lattes/productions-list' }" :exact="true">Productions</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-calendar" :to="{ name: 'lattes/events-list' }" :exact="true">Events</sidenav-router-link>
        <sidenav-router-link icon="ion ion-md-attach" :to="{ name: 'lattes/ct-list' }" :exact="true">CT</sidenav-router-link>
      </sidenav-menu>

    </div>
  </sidenav>
</template>

<script>
import { Sidenav, SidenavLink, SidenavRouterLink, SidenavMenu, SidenavHeader, SidenavBlock, SidenavDivider } from '@/vendor/libs/sidenav'

export default {
  name: 'app-layout-sidenav',
  components: {
    Sidenav,
    SidenavLink,
    SidenavRouterLink,
    SidenavMenu,
    SidenavHeader,
    SidenavBlock,
    SidenavDivider
  },

  props: {
    orientation: {
      type: String,
      default: 'vertical'
    }
  },

  computed: {
    curClasses () {
      let bg = this.layoutSidenavBg

      if (this.orientation === 'horizontal' && (bg.indexOf(' sidenav-dark') !== -1 || bg.indexOf(' sidenav-light') !== -1)) {
        bg = bg
          .replace(' sidenav-dark', '')
          .replace(' sidenav-light', '')
          .replace('-darker', '')
          .replace('-dark', '')
      }

      return `bg-${bg} ` + (
        this.orientation !== 'horizontal'
          ? 'layout-sidenav'
          : 'layout-sidenav-horizontal container-p-x flex-grow-0'
      )
    }
  },

  methods: {
    isMenuActive (url) {
      return this.$route.path.indexOf(url) === 0
    },

    isMenuOpen (url) {
      return this.$route.path.indexOf(url) === 0 && this.orientation !== 'horizontal'
    },

    toggleSidenav () {
      this.layoutHelpers.toggleCollapsed()
    }
  }
}
</script>
