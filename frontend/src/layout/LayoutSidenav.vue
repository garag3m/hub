<template>
  <sidenav :orientation="orientation" class="sidenav sidenav-vertical layout-sidenav bg-white">
    <!-- Brand demo (see src/demo.css) -->
    <div class="app-brand demo" v-if="orientation !== 'horizontal'">
      <span class="app-brand-logo">
        <img :src="`${baseUrl}img/logo reduzida.png`" height="35">
      </span>
      <router-link to="/" class="app-brand-text demo sidenav-text font-weight-normal ml-2">
        livre<br />
        <small style="font-size: 8px;">CENTRO DE ATENÇÃO <br />À MAMA</small>
      </router-link>

      <a href="javascript:void(0)" class="layout-sidenav-toggle sidenav-link text-large ml-auto" @click="toggleSidenav()">
        <i class="ion ion-md-menu align-middle"></i>
      </a>
    </div>
    <div class="sidenav-divider mt-0" v-if="orientation !== 'horizontal'"></div>

    <!-- Inner -->
    <div class="sidenav-inner" :class="{ 'py-1': orientation !== 'horizontal' }">
      <sidenav-router-link icon="ion ion-md-desktop" to="/" :exact="true">Home</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-people" :to="{ name: 'users-list' }" :exact="true">Usuários</sidenav-router-link>
      <sidenav-router-link icon="ion ion-md-people" :to="{ name: 'patients-list' }" :exact="true">Pacientes</sidenav-router-link>

      <!-- aux -->
      <sidenav-menu icon="ion ion-ios-albums" :active="isMenuActive('/aux')" :open="isMenuOpen('/aux')">
        <template slot="link-text">Tabela Auxiliares</template>
        <sidenav-router-link :to="{ name: 'breast-types-list' }" :exact="true">Tipos de Mama</sidenav-router-link>
        <sidenav-router-link :to="{ name: 'categories-radiological-findings-list' }" :exact="true">Categorias de Achado Radiológico</sidenav-router-link>
        <sidenav-router-link :to="{ name: 'location-radiological-findings-list' }" :exact="true">Localizações de Achado</sidenav-router-link>
        <sidenav-router-link :to="{ name: 'skin-types-list' }" :exact="true">Tipos de Pele</sidenav-router-link>
        <sidenav-router-link :to="{ name: 'types-breast-surgeries-list' }" :exact="true">Tipos de Cirurgia Mamária</sidenav-router-link>
        <sidenav-router-link :to="{ name: 'types-radiological-findings-list' }" :exact="true">Tipos de Achado Radiológico</sidenav-router-link>
        <sidenav-router-link :to="{ name: 'types-benign-findings-list' }" :exact="true">Tipos de Achado Benigno</sidenav-router-link>
        <sidenav-router-link :to="{ name: 'results-ultrasound-nodules-list' }" :exact="true">Resultado Nódulo Ultrassom</sidenav-router-link>
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
