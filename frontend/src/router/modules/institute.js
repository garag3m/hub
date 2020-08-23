export default {
    path: 'lattes/institute/',
    component: () => import('@/pages/institute/Index'),
    children: [
      {
        name: 'lattes/institute-list',
        path: 'list',
        component: () => import('@/pages/institute/List')
      }, {
        name: 'lattes/institute-new',
        path: 'new',
        component: () => import('@/pages/institute/New')
      }, {
        name: 'lattes/institute-edit',
        path: ':id/edit',
        component: () => import('@/pages/institute/Edit')
      }
    ]
  }
  