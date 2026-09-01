# Day 01 — Data Acquisition & Professional Formatting

## Goal
Import the raw sales dataset into Excel and turn it into a clean,
professional-looking working sheet — no calculations yet, just structure
and presentation.

## Dataset
`data/sales_data_raw.csv`

## Tasks
1. Import `sales_data_raw.csv` into a new Excel workbook (Data → From Text/CSV).
2. Convert the range into a proper Excel **Table** (Ctrl+T), name it `tbl_Sales`.
3. Apply consistent formatting:
   - Header row bold, filled color, frozen (View → Freeze Panes)
   - `OrderDate` formatted as a real date (not text)
   - `UnitPrice` and `Revenue` formatted as currency
   - `Quantity` as a plain number, right-aligned
4. Auto-fit all column widths.
5. Add a second sheet named `Notes` describing what you observed about
   data quality (don't fix anything yet — just note it): are there blanks?
   Inconsistent casing? Multiple date formats?
6. Save as `day01_solved.xlsx`.

## Deliverable
`day01_solved.xlsx` with a formatted `tbl_Sales` table and a `Notes` sheet.

## Why this matters
Every analysis starts with import + formatting. Getting this step wrong
(text-formatted dates, inconsistent types) breaks every formula downstream.
