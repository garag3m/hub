export default {
  path: 'types-benign-findings/',
  component: () => import('@/pages/types_benign_findings/Index'),
  children: [
    {
      name: 'types-benign-findings-list',
      path: 'list',
      component: () => import('@/pages/types_benign_findings/List')
    }, {
      name: 'types-benign-findings-new',
      path: 'new',
      component: () => import('@/pages/types_benign_findings/New')
    }, {
      name: 'types-benign-findings-edit',
      path: ':id/edit',
      component: () => import('@/pages/types_benign_findings/Edit')
    }
  ]
}
