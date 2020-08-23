export default {
    path: 'lattes/awards/',
    component: () => import('@/pages/awards/Index'),
    children: [
      {
        name: 'lattes/awards-list',
        path: 'list',
        component: () => import('@/pages/awards/List')
      }, {
        name: 'lattes/awards-new',
        path: 'new',
        component: () => import('@/pages/awards/New')
      }, {
        name: 'lattes/awards-edit',
        path: ':id/edit',
        component: () => import('@/pages/awards/Edit')
      }
    ]
  }
  