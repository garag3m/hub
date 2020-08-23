export default {
    path: 'lattes/ct/',
    component: () => import('@/pages/ct/Index'),
    children: [
      {
        name: 'lattes/ct-list',
        path: 'list',
        component: () => import('@/pages/ct/List')
      }, {
        name: 'lattes/ct-new',
        path: 'new',
        component: () => import('@/pages/ct/New')
      }, {
        name: 'lattes/ct-edit',
        path: ':id/edit',
        component: () => import('@/pages/ct/Edit')
      }
    ]
  }
  