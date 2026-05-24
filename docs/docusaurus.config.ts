import {themes as prismThemes} from "prism-react-renderer";
import type {Config} from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "End-to-End Recommendation System",
  tagline: "A production-minded blueprint for understanding data, training retrieval, and serving recommendations.",
  favicon: "img/recsys-mark.svg",

  future: {
    v4: true
  },

  url: "https://example.com",
  baseUrl: "/",

  organizationName: "nickward",
  projectName: "end2end-recommendation-system",

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "en",
    locales: ["en"]
  },

  presets: [
    [
      "classic",
      {
        docs: {
          path: "content",
          routeBasePath: "guide",
          sidebarPath: "./sidebars.ts",
          breadcrumbs: true
        },
        blog: false,
        pages: true,
        theme: {
          customCss: "./src/css/custom.css"
        }
      } satisfies Preset.Options
    ]
  ],

  themeConfig: {
    navbar: {
      title: "RecSys Blueprint",
      logo: {
        alt: "Recommendation system logo",
        src: "img/recsys-mark.svg"
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Documentation"
        },
        {
          to: "/guide/understanding-the-data/overview",
          label: "Understanding the Data",
          position: "left"
        },
        {
          href: "https://github.com/nickward/end2end-recommendation-system",
          label: "GitHub",
          position: "right"
        }
      ]
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Guide",
          items: [
            {
              label: "Start Here",
              to: "/guide/understanding-the-data/overview"
            }
          ]
        },
        {
          title: "Roadmap",
          items: [
            {
              label: "Retrieval and Ranking",
              to: "/"
            }
          ]
        }
      ],
      copyright: `Built for ${new Date().getFullYear()} recommendation system documentation.`
    },
    docs: {
      sidebar: {
        hideable: true
      }
    },
    colorMode: {
      respectPrefersColorScheme: false,
      defaultMode: "light"
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ["python", "bash", "json"]
    }
  } satisfies Preset.ThemeConfig
};

export default config;
