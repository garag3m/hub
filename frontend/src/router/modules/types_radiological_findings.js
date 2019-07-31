export default {
  path: 'types-radiological-findings/',
  component: () => import('@/pages/types_radiological_findings/Index'),
  children: [
    {
      name: 'types-radiological-findings-list',
      path: 'list',
      component: () => import('@/pages/types_radiological_findings/List')
    }, {
      name: 'types-radiological-findings-new',
      path: 'new',
      component: () => import('@/pages/types_radiological_findings/New')
    }, {
      name: 'types-radiological-findings-edit',
      path: ':id/edit',
      component: () => import('@/pages/types_radiological_findings/Edit')
    }
  ]
}
