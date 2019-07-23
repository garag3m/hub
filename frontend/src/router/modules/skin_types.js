export default {
  path: 'skin-types/',
  component: () => import('@/pages/skin_types/Index'),
  children: [
    {
      name: 'skin-types-list',
      path: 'list',
      component: () => import('@/pages/skin_types/List')
    }, {
      name: 'skin-types-new',
      path: 'new',
      component: () => import('@/pages/skin_types/New')
    }, {
      name: 'skin-types-edit',
      path: ':id/edit',
      component: () => import('@/pages/skin_types/Edit')
    }
  ]
}
