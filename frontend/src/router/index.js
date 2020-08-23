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
import instituteRoutes from './modules/institute.js'
import addressRoutes from './modules/address.js'
import academicEducationRoutes from './modules/academic_education.js'
import complementaryEducationRoutes from './modules/complementary_education.js'
import taskRoutes from './modules/task.js'
import professionalPerformanceRoutes from './modules/professional_performance.js'
import teachingProjectsRoutes from './modules/teaching_projects.js'
import languagesRoutes from './modules/languages.js'
import awardsRoutes from './modules/awards.js'
import productionsRoutes from './modules/productions.js'
import eventsRoutes from './modules/events.js'
import ctRoutes from './modules/ct.js'
import personRoutes from './modules/person.js'

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
      .concat(instituteRoutes)
      .concat(addressRoutes)
      .concat(academicEducationRoutes)
      .concat(complementaryEducationRoutes)
      .concat(taskRoutes)
      .concat(professionalPerformanceRoutes)
      .concat(teachingProjectsRoutes)
      .concat(languagesRoutes)
      .concat(awardsRoutes)
      .concat(productionsRoutes)
      .concat(eventsRoutes)
      .concat(ctRoutes)
      .concat(personRoutes)
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
