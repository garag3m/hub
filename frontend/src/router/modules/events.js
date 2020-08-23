export default {
    path: 'lattes/events/',
    component: () => import('@/pages/events/Index'),
    children: [
      {
        name: 'lattes/events-list',
        path: 'list',
        component: () => import('@/pages/events/List')
      }, {
        name: 'lattes/events-new',
        path: 'new',
        component: () => import('@/pages/events/New')
      }, {
        name: 'lattes/events-edit',
        path: ':id/edit',
        component: () => import('@/pages/events/Edit')
      }
    ]
  }
  