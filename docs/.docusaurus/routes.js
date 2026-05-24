import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/guide',
    component: ComponentCreator('/guide', 'a20'),
    routes: [
      {
        path: '/guide',
        component: ComponentCreator('/guide', '337'),
        routes: [
          {
            path: '/guide',
            component: ComponentCreator('/guide', '363'),
            routes: [
              {
                path: '/guide/understanding-the-data/overview',
                component: ComponentCreator('/guide/understanding-the-data/overview', 'f42'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/guide/understanding-the-data/quality-checks',
                component: ComponentCreator('/guide/understanding-the-data/quality-checks', '547'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/guide/understanding-the-data/schema-and-granularity',
                component: ComponentCreator('/guide/understanding-the-data/schema-and-granularity', '555'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/guide/understanding-the-data/source-assets',
                component: ComponentCreator('/guide/understanding-the-data/source-assets', 'ff3'),
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
    path: '/',
    component: ComponentCreator('/', 'e5f'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
