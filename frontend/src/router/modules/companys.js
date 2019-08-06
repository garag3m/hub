export default {
    path: 'companys/',
    component: () => import('@/pages/companys/Index'),
    children: [
      {
        name: 'companys-list',
        path: 'list',
        component: () => import('@/pages/companys/List')
      }, {
        name: 'companys-new',
        path: 'new',
        component: () => import('@/pages/companys/New')
      }, {
        name: 'companys-edit',
        path: ':id/edit',
        component: () => import('@/pages/companys/Edit')
      }
    ]
  }
  