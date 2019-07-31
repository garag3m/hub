export default {
  path: 'breast-types/',
  component: () => import('@/pages/breast_types/Index'),
  children: [
    {
      name: 'breast-types-list',
      path: 'list',
      component: () => import('@/pages/breast_types/List')
    }, {
      name: 'breast-types-new',
      path: 'new',
      component: () => import('@/pages/breast_types/New')
    }, {
      name: 'breast-types-edit',
      path: ':id/edit',
      component: () => import('@/pages/breast_types/Edit')
    }
  ]
}
