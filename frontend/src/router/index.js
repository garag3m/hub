import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'

import globals from '@/globals'

// Layouts
import Layout2 from '@/layout/Layout2'

// Routes
import authRoutes from './auth.js'
import userRoutes from './modules/users.js'
import patientRoutes from './modules/patients.js'
import breastTypeRoutes from './modules/breast_types.js'
import categoriesRadiologicalFindingRoutes from './modules/categories_radiological_findings.js'
import locationRadiologicalFindingRoutes from './modules/location_radiological_findings.js'
import resultUltrasoundNoduleRoutes from './modules/results_ultrasound_nodules.js'
import skinTypeRoutes from './modules/skin_types.js'
import typeBenignFindingRoutes from './modules/types_benign_findings.js'
import typeBreastSurgeryRoutes from './modules/types_breast_surgeries.js'
import typeRadiologicalFindingRoutes from './modules/types_radiological_findings.js'

// Middlewares
import authMiddleware from './middlewares/auth.js'

Vue.use(Router)
Vue.use(Meta)

const ROUTES = [
  {
    path: '/',
    component: Layout2,
    children: [
      {
        name: 'home',
        path: '',
        component: () => import('@/pages/Home')
      }
    ]
      .concat(userRoutes)
      .concat(patientRoutes)
      .concat(breastTypeRoutes)
      .concat(categoriesRadiologicalFindingRoutes)
      .concat(locationRadiologicalFindingRoutes)
      .concat(resultUltrasoundNoduleRoutes)
      .concat(skinTypeRoutes)
      .concat(typeBenignFindingRoutes)
      .concat(typeBreastSurgeryRoutes)
      .concat(typeRadiologicalFindingRoutes)
  }
]
  .concat(authRoutes)

const router = new Router({
  base: '/',
  mode: 'history',
  routes: ROUTES
})

router.afterEach(() => {
  // On small screens collapse sidenav
  if (window.layoutHelpers && window.layoutHelpers.isSmallScreen() && !window.layoutHelpers.isCollapsed()) {
    setTimeout(() => window.layoutHelpers.setCollapsed(true, true), 10)
  }

  // Scroll to top of the page
  globals().scrollTop(0, 0)
})

router.beforeEach((to, from, next) => {
  const context = { to, from, next }
  authMiddleware(context)

  // Set loading state
  document.body.classList.add('app-loading')

  // Add tiny timeout to finish page transition
  setTimeout(() => next(), 10)
})

export default router
