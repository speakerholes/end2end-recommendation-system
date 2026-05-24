import Link from "@docusaurus/Link";
import Layout from "@theme/Layout";
import clsx from "clsx";
import styles from "./index.module.css";

const pillars = [
  {
    title: "Ground the system in data reality",
    description:
      "Start with the real shape of Amazon reviews and metadata before making modeling assumptions."
  },
  {
    title: "Design for retrieval at scale",
    description:
      "Leave room for candidate generation, feature pipelines, and a two-tower architecture without rewriting the narrative."
  },
  {
    title: "Document like an engineering artifact",
    description:
      "Treat the site as a durable technical reference, not a pile of disconnected notes."
  }
];

export default function Home(): JSX.Element {
  return (
    <Layout
      title="Recommendation System Docs"
      description="Beautiful technical documentation for an end-to-end recommendation system."
    >
      <main className={styles.page}>
        <section className={styles.hero}>
          <div className={styles.heroCopy}>
            <p className={styles.kicker}>End-to-End Recommendation System</p>
            <h1>Technical documentation built to grow into a full recommender blueprint.</h1>
            <p className={styles.summary}>
              The site starts with data understanding because every reliable retrieval and ranking
              stack depends on clear semantics, healthy joins, and realistic assumptions about user
              behavior.
            </p>
            <div className={styles.actions}>
              <Link className="button button--primary button--lg" to="/guide/understanding-the-data/overview">
                Read the data guide
              </Link>
              <Link className={clsx("button button--secondary button--lg", styles.ghostButton)} to="/guide/understanding-the-data/quality-checks">
                Review quality checks
              </Link>
            </div>
          </div>
          <div className={styles.heroPanel}>
            <div className={styles.panelGlow} />
            <div className={styles.metricCard}>
              <span>Current scope</span>
              <strong>Understanding the data</strong>
            </div>
            <div className={styles.roadmapCard}>
              <p>Planned expansion</p>
              <ul>
                <li>Feature engineering</li>
                <li>Two-tower retrieval</li>
                <li>Evaluation and offline metrics</li>
                <li>Serving and monitoring</li>
              </ul>
            </div>
          </div>
        </section>

        <section className={styles.pillars}>
          {pillars.map((pillar) => (
            <article key={pillar.title} className={styles.pillarCard}>
              <h2>{pillar.title}</h2>
              <p>{pillar.description}</p>
            </article>
          ))}
        </section>
      </main>
    </Layout>
  );
}
