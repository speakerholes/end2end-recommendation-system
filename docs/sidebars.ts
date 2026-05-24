import type {SidebarsConfig} from "@docusaurus/plugin-content-docs";

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: "category",
      label: "Understanding the Data",
      link: {
        type: "doc",
        id: "understanding-the-data/overview"
      },
      items: [
        "understanding-the-data/overview",
        "understanding-the-data/source-assets",
        "understanding-the-data/schema-and-granularity",
        "understanding-the-data/quality-checks"
      ]
    }
  ]
};

export default sidebars;
