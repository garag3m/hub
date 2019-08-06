export default {
    path: 'meals/',
    component: () => import('@/pages/meals/Index'),
    children: [
      {
        name: 'meals-list',
        path: 'list',
        component: () => import('@/pages/meals/List')
      }, {
        name: 'meals-new',
        path: 'new',
        component: () => import('@/pages/meals/New')
      }, {
        name: 'meals-edit',
        path: ':id/edit',
        component: () => import('@/pages/meals/Edit')
      }
    ]
  }
  