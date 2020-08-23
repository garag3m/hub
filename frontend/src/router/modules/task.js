export default {
    path: 'lattes/task/',
    component: () => import('@/pages/task/Index'),
    children: [
      {
        name: 'lattes/task-list',
        path: 'list',
        component: () => import('@/pages/task/List')
      }, {
        name: 'lattes/task-new',
        path: 'new',
        component: () => import('@/pages/task/New')
      }, {
        name: 'lattes/task-edit',
        path: ':id/edit',
        component: () => import('@/pages/task/Edit')
      }
    ]
  }
  