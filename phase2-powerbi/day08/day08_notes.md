# Day 08 — Power BI Interface & Report View: Solution Notes

## The three views

**Report view** — where you build the actual visuals: charts, tables, cards,
slicers. This is what end users see when the dashboard is shared. You drag
fields from the Data pane onto the canvas here.

**Data view** — a spreadsheet-like view of every table currently loaded into
the model. Useful for spot-checking that a column loaded correctly, or for
quickly eyeballing values without building a visual. You can also create
calculated columns from here.

**Model view** — shows every table as a box, and the relationships between
them as connecting lines. This is where you build/inspect your data model
(the same star-schema concept from Day 10). If a report visual is showing
wrong or duplicated numbers, Model view is usually where the bug lives (a
missing or wrong-direction relationship).

## Setup steps for this file
1. Get Data → Text/CSV → select `data/sales_data_clean.csv` → Load
2. In Report view, rename Page 1 to "Overview"
3. Add a Card visual → drag `Revenue` into it → shows Total Revenue by default (SUM)
4. Add a Bar Chart → Axis: `Region`, Values: `Revenue`
5. Add a Table visual → drag several raw columns in to see the underlying rows

## Deliverable note
`.pbix` files are a proprietary Microsoft binary format that can't be
generated outside Power BI Desktop itself. This solution folder instead
ships the exact Power Query M code / DAX / build steps for every Power BI
day (08–14) as plain text — paste these directly into Power BI Desktop
(Home → Transform Data → Advanced Editor for M code, or New Measure for
DAX) and you'll get an identical result to what the task asks for.
