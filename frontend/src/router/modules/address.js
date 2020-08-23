export default {
  path: 'address/',
  component: () => import('@/pages/address/Index'),
  children: [
    {
      name: 'address-list',
      path: 'list',
      component: () => import('@/pages/address/List')
    }, {
      name: 'address-new',
      path: 'new',
      component: () => import('@/pages/address/New')
    }, {
      name: 'address-edit',
      path: ':id/edit',
      component: () => import('@/pages/address/Edit')
    }
  ]
}
