# Capstone Summary — SQL → Python → BI Dashboard

## What this pipeline does end-to-end

1. **SQL** (`capstone_clean.sql`) loads the raw, messy sales export
   (`sales_data_raw.csv`, 3,040 rows) into SQLite, removes ~40 duplicate
   `OrderID` rows, standardizes `Region`/`Channel` text casing, and fills
   missing `Region`, `SalesRep`, `UnitPrice`, and `Quantity` values —
   producing a clean `sales_clean` table (3,000 rows, zero remaining nulls
   in those columns).

2. **Python** (`capstone_analysis.py`) connects to that SQLite database
   with `pandas.read_sql()`, parses the still-mixed `OrderDate` formats,
   and layers on two new features: an `EstimatedProfit` column (30% margin
   assumed on Electronics/Furniture, 15% on Grocery/Apparel/Stationery)
   and an `OrderSegment` label (Small/Medium/Large by quantity). It runs
   the full analysis — top products, regional performance, monthly trend,
   year-over-year growth — then exports the final analysis-ready table to
   `data/sales_data_capstone_final.csv`.

3. **BI Dashboard** (`capstone_dashboard.xlsx`) imports that final CSV and
   builds a one-page view: 4 KPI cards (Total Revenue, Total Orders,
   Average Order Value, YoY Growth), a Revenue-by-Region bar chart, a
   Revenue-by-Category bar chart, a 24-month revenue trend line chart, and
   a Top 10 Products table — all driven by live formulas against the
   underlying data table.

## 3 key findings

1. **South is the top-performing region** by total revenue, edging out
   East and West, while the North and Central regions trail behind it —
   worth investigating what South's sales reps or channel mix are doing
   differently.
2. **Electronics is the leading category by a wide margin**, driven by
   high-ticket items (Laptop, Smartphone) rather than order volume — a
   small number of big-ticket sales categories account for a
   disproportionate share of total revenue.
3. **Year-over-year revenue was roughly flat to slightly down (~-3%)**
   from 2024 to 2025 across the full dataset — growth wasn't uniform
   month to month, and a few strong months (e.g. peaks in spring) were
   offset by weaker mid-year months, suggesting seasonality worth
   planning around rather than a straight decline.

## Files in this folder
- `capstone_clean.sql` — SQL cleaning script (tested against SQLite)
- `capstone_analysis.py` — Python analysis + feature engineering pipeline
- `build_capstone_dashboard.py` — script that generates the dashboard
- `capstone_dashboard.xlsx` — the final one-page BI dashboard 
  (built in Excel rather than Power BI's `.pbix` format, since `.pbix`
  is a proprietary binary that can only be produced inside Power BI
  Desktop itself — the Power BI *logic* for an equivalent dashboard is
  documented throughout `phase2-powerbi/`)


