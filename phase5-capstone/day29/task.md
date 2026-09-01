# Day 29 — Capstone Project: SQL → Python → BI Dashboard

## Goal
Build one end-to-end pipeline that touches every skill from the last
28 days, using the raw dataset as the single source of truth.

## Pipeline
1. **SQL**: Load `data/sales_data_raw.csv` into a SQLite database.
   Write cleaning queries (dedupe, standardize text, handle blanks) to
   produce a clean `sales_clean` table.
2. **Python**: Connect to that database with Pandas, pull `sales_clean`,
   and run a full analysis — top products, regional performance, monthly
   trends, and at least one further engineered feature (e.g. profit
   estimate, customer segment by order size).
3. **Export**: Save the final analysis-ready DataFrame back out as
   `data/sales_data_capstone_final.csv`.
4. **BI Dashboard**: Import that final CSV into Power BI (or rebuild your
   Day 07 Excel dashboard using it) — a one-page view with:
   - KPI cards: Total Revenue, Total Orders, Avg Order Value, YoY Growth
   - Revenue trend by month
   - Revenue by Region and Category
   - Top 10 Products table
   - At least one slicer/filter

## Tasks
1. Write the SQL cleaning script: `capstone_clean.sql`
2. Write the Python analysis pipeline: `capstone_analysis.py`
3. Build the dashboard: `capstone_dashboard.pbix` (or `.xlsx`)
4. Write a `CAPSTONE_SUMMARY.md`: what the pipeline does end-to-end, 3
   key findings, and a screenshot (or description) of the final dashboard.

## Deliverable
All four files above in `phase5-capstone/day29/`.

## Why this matters
This is the project you lead with when someone asks "what have you built?"
— it demonstrates the full stack: database → code → business-facing output.
