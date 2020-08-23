export default {
    path: 'lattes/complementary-education/',
    component: () => import('@/pages/complementary_education/Index'),
    children: [
      {
        name: 'lattes/complementary-education-list',
        path: 'list',
        component: () => import('@/pages/complementary_education/List')
      }, {
        name: 'lattes/complementary-education-new',
        path: 'new',
        component: () => import('@/pages/complementary_education/New')
      }, {
        name: 'lattes/complementary-education-edit',
        path: ':id/edit',
        component: () => import('@/pages/complementary_education/Edit')
      }
    ]
  }
  