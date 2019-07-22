<template>
  <nav class="layout-footer footer" :class="getLayoutFooterBg()">
    <div class="container-fluid container-p-x pb-3">
    </div>
  </nav>
</template>

<script>
export default {
  name: 'app-layout-footer',

  methods: {
    getLayoutFooterBg () {
      return `bg-${this.layoutFooterBg}`
    }
  }
}
</script>
