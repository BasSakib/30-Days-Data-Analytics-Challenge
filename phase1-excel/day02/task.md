# Day 02 — Logic & Calculations

## Goal
Build a sales summary using SUM, AVERAGE, and IF logic.

## Dataset
Use `day01_solved.xlsx` (or `sales_data_raw.csv` if starting fresh) as your base.

## Tasks
1. On a new sheet `Summary`, calculate:
   - Total Revenue (`SUM`)
   - Average Order Value (`AVERAGE` of Revenue)
   - Total Quantity Sold (`SUM`)
   - Number of Orders (`COUNTA` or `COUNT`)
2. Add a column `OrderSize` next to the sales table using `IF`:
   - "Large" if `Quantity >= 15`
   - "Medium" if `Quantity >= 5` and `< 15`
   - "Small" if `Quantity < 5`
3. Add a column `HighValue` using `IF`: "Yes" if `Revenue > 500`, else "No".
4. On `Summary`, count how many orders are "Large" vs "Medium" vs "Small"
   using `COUNTIF`.
5. Save as `day02_solved.xlsx`.

## Deliverable
`day02_solved.xlsx` with a `Summary` sheet and two new logic-driven columns
in the sales table.
