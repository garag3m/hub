export default {
    path: 'stages/',
    component: () => import('@/pages/stages/Index'),
    children: [
      {
        name: 'stages-list',
        path: 'list',
        component: () => import('@/pages/stages/List')
      }, {
        name: 'stages-new',
        path: 'new',
        component: () => import('@/pages/stages/New')
      }, {
        name: 'stages-edit',
        path: ':id/edit',
        component: () => import('@/pages/stages/Edit')
      }
    ]
  }
  