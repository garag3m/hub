export default {
  path: 'patients/',
  component: () => import('@/pages/patients/Index'),
  children: [
    {
      name: 'patients-list',
      path: 'list',
      component: () => import('@/pages/patients/List')
    }, {
      name: 'patients-new',
      path: 'new',
      component: () => import('@/pages/patients/New')
    }, {
      name: 'patients-edit',
      path: ':id/edit',
      component: () => import('@/pages/patients/Edit')
    }
  ]
}
