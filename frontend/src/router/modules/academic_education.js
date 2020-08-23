export default {
    path: 'lattes/academic-education/',
    component: () => import('@/pages/academic_education/Index'),
    children: [
      {
        name: 'lattes/academic-education-list',
        path: 'list',
        component: () => import('@/pages/academic_education/List')
      }, {
        name: 'lattes/academic-education-new',
        path: 'new',
        component: () => import('@/pages/academic_education/New')
      }, {
        name: 'lattes/academic-education-edit',
        path: ':id/edit',
        component: () => import('@/pages/academic_education/Edit')
      }
    ]
  }
  