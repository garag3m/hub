export default {
    path: 'lattes/professional-performance/',
    component: () => import('@/pages/professional_performance/Index'),
    children: [
      {
        name: 'lattes/professional-performance-list',
        path: 'list',
        component: () => import('@/pages/professional_performance/List')
      }, {
        name: 'lattes/professional-performance-new',
        path: 'new',
        component: () => import('@/pages/professional_performance/New')
      }, {
        name: 'lattes/professional-performance-edit',
        path: ':id/edit',
        component: () => import('@/pages/professional_performance/Edit')
      }
    ]
  }
  