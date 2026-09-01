# Day 05 — Dimensional Analysis with Pivot Tables

## Goal
Use Pivot Tables to slice the cleaned dataset by region and product.

## Dataset
Use your cleaned data from Day 04 (or `data/sales_data_clean.csv`).

## Tasks
1. Insert a Pivot Table on a new sheet `PivotAnalysis`.
2. Build these four views (can be four separate pivot tables on the same sheet):
   - **Revenue by Region** (Rows: Region, Values: Sum of Revenue)
   - **Revenue by Category** (Rows: Category, Values: Sum of Revenue)
   - **Revenue by Region + Category** (Rows: Region, Columns: Category)
   - **Top 5 SalesReps by Revenue** (Rows: SalesRep, Values: Sum of Revenue,
     sorted descending, filtered to top 5)
3. Add at least one **Pivot Chart** (bar chart of Revenue by Region).
4. Add a **Slicer** for `Channel` and connect it to all pivot tables.
5. Save as `day05_solved.xlsx`.

## Deliverable
`day05_solved.xlsx` with 4 pivot views, 1 pivot chart, and a working slicer.
