export default {
  path: 'location-radiological-findings/',
  component: () => import('@/pages/location_radiological_findings/Index'),
  children: [
    {
      name: 'location-radiological-findings-list',
      path: 'list',
      component: () => import('@/pages/location_radiological_findings/List')
    }, {
      name: 'location-radiological-findings-new',
      path: 'new',
      component: () => import('@/pages/location_radiological_findings/New')
    }, {
      name: 'location-radiological-findings-edit',
      path: ':id/edit',
      component: () => import('@/pages/location_radiological_findings/Edit')
    }
  ]
}
