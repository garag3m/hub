import LayoutBlank from '@/layout/LayoutBlank'

export default {
  path: '/auth',
  component: LayoutBlank,
  children: [
    {
      name: 'login',
      path: '/login',
      component: () => import('@/pages/auth/Login')
    }, {
      name: 'register',
      path: '/register',
      component: () => import('@/pages/auth/Register')
    }
  ]
}
