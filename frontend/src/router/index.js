import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'

import globals from '@/globals'

// Layouts
import Layout2 from '@/layout/Layout2'

// Routes
import authRoutes from './auth.js'
import userRoutes from './modules/users.js'
import studentsRoutes from './modules/students.js'
import requestsRoutes from './modules/requests.js'
import mealsRoutes from './modules/meals.js'
import companysRoutes from './modules/companys.js'
import stagesRoutes from './modules/stages.js'
import documentOpinionsRoutes from './modules/document_opinions.js'
import filesRoutes from './modules/files.js'

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
      .concat(studentsRoutes)
      .concat(requestsRoutes)
      .concat(mealsRoutes)
      .concat(companysRoutes)
      .concat(stagesRoutes)
      .concat(documentOpinionsRoutes)
      .concat(filesRoutes)
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
