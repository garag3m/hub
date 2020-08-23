export default {
    path: 'lattes/languages/',
    component: () => import('@/pages/languages/Index'),
    children: [
      {
        name: 'lattes/languages-list',
        path: 'list',
        component: () => import('@/pages/languages/List')
      }, {
        name: 'lattes/languages-new',
        path: 'new',
        component: () => import('@/pages/languages/New')
      }, {
        name: 'lattes/languages-edit',
        path: ':id/edit',
        component: () => import('@/pages/languages/Edit')
      }
    ]
  }
  