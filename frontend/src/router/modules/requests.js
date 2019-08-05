export default {
    path: 'requests/',
    component: () => import('@/pages/requests/Index'),
    children: [
      {
        name: 'requests-list',
        path: 'list',
        component: () => import('@/pages/requests/List')
      }, {
        name: 'requests-new',
        path: 'new',
        component: () => import('@/pages/requests/New')
      }, {
        name: 'requests-edit',
        path: ':id/edit',
        component: () => import('@/pages/requests/Edit')
      }
    ]
  }
  