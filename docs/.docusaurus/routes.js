import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/end2end-recommendation-system/guide',
    component: ComponentCreator('/end2end-recommendation-system/guide', 'de3'),
    routes: [
      {
        path: '/end2end-recommendation-system/guide',
        component: ComponentCreator('/end2end-recommendation-system/guide', '0cd'),
        routes: [
          {
            path: '/end2end-recommendation-system/guide',
            component: ComponentCreator('/end2end-recommendation-system/guide', '88a'),
            routes: [
              {
                path: '/end2end-recommendation-system/guide/understanding-the-data/overview',
                component: ComponentCreator('/end2end-recommendation-system/guide/understanding-the-data/overview', '120'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/end2end-recommendation-system/guide/understanding-the-data/quality-checks',
                component: ComponentCreator('/end2end-recommendation-system/guide/understanding-the-data/quality-checks', '0c2'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/end2end-recommendation-system/guide/understanding-the-data/schema-and-granularity',
                component: ComponentCreator('/end2end-recommendation-system/guide/understanding-the-data/schema-and-granularity', '5cf'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/end2end-recommendation-system/guide/understanding-the-data/source-assets',
                component: ComponentCreator('/end2end-recommendation-system/guide/understanding-the-data/source-assets', 'd24'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/end2end-recommendation-system/',
    component: ComponentCreator('/end2end-recommendation-system/', 'a0c'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
