export default {
  path: 'categories-radiological-findings/',
  component: () => import('@/pages/categories_radiological_findings/Index'),
  children: [
    {
      name: 'categories-radiological-findings-list',
      path: 'list',
      component: () => import('@/pages/categories_radiological_findings/List')
    }, {
      name: 'categories-radiological-findings-new',
      path: 'new',
      component: () => import('@/pages/categories_radiological_findings/New')
    }, {
      name: 'categories-radiological-findings-edit',
      path: ':id/edit',
      component: () => import('@/pages/categories_radiological_findings/Edit')
    }
  ]
}
