export default {
    path: 'lattes/teaching-projects/',
    component: () => import('@/pages/teaching_projects/Index'),
    children: [
      {
        name: 'lattes/teaching-projects-list',
        path: 'list',
        component: () => import('@/pages/teaching_projects/List')
      }, {
        name: 'lattes/teaching-projects-new',
        path: 'new',
        component: () => import('@/pages/teaching_projects/New')
      }, {
        name: 'lattes/teaching-projects-edit',
        path: ':id/edit',
        component: () => import('@/pages/teaching_projects/Edit')
      }
    ]
  }
  