export default {
    path: 'lattes/person/',
    component: () => import('@/pages/person/Index'),
    children: [
      {
        name: 'lattes/person-list',
        path: 'list',
        component: () => import('@/pages/person/List')
      }, {
        name: 'lattes/person-new',
        path: 'new',
        component: () => import('@/pages/person/New')
      }, {
        name: 'lattes/person-edit',
        path: ':id/edit',
        component: () => import('@/pages/person/Edit')
      }
    ]
  }
  