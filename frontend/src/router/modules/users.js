export default {
  path: 'users/',
  component: () => import('@/pages/users/Index'),
  children: [
    {
      name: 'users-list',
      path: 'list',
      component: () => import('@/pages/users/List')
    }, {
      name: 'users-new',
      path: 'new',
      component: () => import('@/pages/users/New')
    }, {
      name: 'users-edit',
      path: ':id/edit',
      component: () => import('@/pages/users/Edit')
    }
  ]
}
