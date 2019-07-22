export default {
  path: 'types-breast-surgeries/',
  component: () => import('@/pages/types_breast_surgeries/Index'),
  children: [
    {
      name: 'types-breast-surgeries-list',
      path: 'list',
      component: () => import('@/pages/types_breast_surgeries/List')
    }, {
      name: 'types-breast-surgeries-new',
      path: 'new',
      component: () => import('@/pages/types_breast_surgeries/New')
    }, {
      name: 'types-breast-surgeries-edit',
      path: ':id/edit',
      component: () => import('@/pages/types_breast_surgeries/Edit')
    }
  ]
}
