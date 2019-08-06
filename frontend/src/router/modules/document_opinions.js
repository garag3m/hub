export default {
    path: 'document-opinions/',
    component: () => import('@/pages/document_opinions/Index'),
    children: [
      {
        name: 'document-opinions-list',
        path: 'list',
        component: () => import('@/pages/document_opinions/List')
      }, {
        name: 'document-opinions-new',
        path: 'new',
        component: () => import('@/pages/document_opinions/New')
      }, {
        name: 'document-opinions-edit',
        path: ':id/edit',
        component: () => import('@/pages/document_opinions/Edit')
      }
    ]
  }
  