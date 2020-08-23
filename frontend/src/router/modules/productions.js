export default {
    path: 'lattes/productions/',
    component: () => import('@/pages/productions/Index'),
    children: [
      {
        name: 'lattes/productions-list',
        path: 'list',
        component: () => import('@/pages/productions/List')
      }, {
        name: 'lattes/productions-new',
        path: 'new',
        component: () => import('@/pages/productions/New')
      }, {
        name: 'lattes/productions-edit',
        path: ':id/edit',
        component: () => import('@/pages/productions/Edit')
      }
    ]
  }
  