export default {
    path: 'files/',
    component: () => import('@/pages/files/Index'),
    children: [
      {
        name: 'files-list',
        path: 'list',
        component: () => import('@/pages/files/List')
      }, {
        name: 'files-new',
        path: 'new',
        component: () => import('@/pages/files/New')
      }, {
        name: 'files-edit',
        path: ':id/edit',
        component: () => import('@/pages/files/Edit')
      }
    ]
  }
  