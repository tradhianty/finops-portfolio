# FinOps Portfolio – Starter Kit

This repo scaffolds a public, reproducible FinOps portfolio with **free-first tools**.

## What’s inside
- `data/synthetic/`: synthetic billing dataset (GCP-like schema)
- `scripts/`: generators + sample anomaly detector + chargeback example
- `models/`: space for dbt/DuckDB SQL transforms
- `dashboards/looker_studio/`: notes to wire a dashboard
- `reports/templates/`: case study + executive MBR templates
- `website/`: simple landing page for GitHub Pages

## Quick start
1. Create a new public GitHub repo and upload these files.
2. (Optional) Load `data/synthetic/gcp_billing_sample.csv` into **BigQuery Sandbox** or **DuckDB**.
3. Open Looker Studio and connect to the CSV/Sheet to build the dashboard.
4. Fill out `reports/case-studies/52pct_savings_case_study.md` with your specifics and screenshots.
5. Turn on **GitHub Pages** to publish `/website`.

## Free Tools
GitHub, GitHub Pages, Google Sheets, Looker Studio, DuckDB or BigQuery Sandbox, Python (pandas/statsmodels), OpenCost, Grafana OSS, dbt Core (optional).
