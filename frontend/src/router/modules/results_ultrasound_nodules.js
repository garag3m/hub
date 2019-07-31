export default {
  path: 'results-ultrasound-nodules/',
  component: () => import('@/pages/results_ultrasound_nodules/Index'),
  children: [
    {
      name: 'results-ultrasound-nodules-list',
      path: 'list',
      component: () => import('@/pages/results_ultrasound_nodules/List')
    }, {
      name: 'results-ultrasound-nodules-new',
      path: 'new',
      component: () => import('@/pages/results_ultrasound_nodules/New')
    }, {
      name: 'results-ultrasound-nodules-edit',
      path: ':id/edit',
      component: () => import('@/pages/results_ultrasound_nodules/Edit')
    }
  ]
}
