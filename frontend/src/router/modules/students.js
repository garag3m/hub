export default {
    path: 'students/',
    component: () => import('@/pages/students/Index'),
    children: [
      {
        name: 'students-list',
        path: 'list',
        component: () => import('@/pages/students/List')
      }, {
        name: 'students-new',
        path: 'new',
        component: () => import('@/pages/students/New')
      }, {
        name: 'students-edit',
        path: ':id/edit',
        component: () => import('@/pages/students/Edit')
      }
    ]
  }
  