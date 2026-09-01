# Day 25 — Exploratory Data Analysis (EDA)

## Goal
Dig into the cleaned dataset for real patterns.

## Dataset
Your Day 24 cleaned output (or `data/sales_data_clean.csv`).

## Tasks
1. Revenue distribution: describe(), skew, and a rough sense of outliers
   (IQR method — flag orders beyond 1.5×IQR).
2. Correlation: numeric columns correlation matrix (`Quantity`,
   `UnitPrice`, `Revenue`).
3. Group-level patterns:
   - Revenue by Region (groupby + sum, sorted)
   - Revenue by Category (groupby + sum, sorted)
   - Average order value by Channel
4. Time patterns: revenue by month, revenue by weekday.
5. Write 5 bullet-point findings in plain English at the end of the script
   (e.g., "Electronics has the highest average order value at $X, driven
   by Laptop and Smartphone sales").

## Deliverable
`day25_solved.py` with analysis code and a findings summary printed at the end.
