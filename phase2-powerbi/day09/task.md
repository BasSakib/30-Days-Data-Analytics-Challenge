# Day 09 — Power Query: Complex Transforms & Cleaning

## Goal
Do the full cleaning pipeline inside Power BI's Power Query editor, this
time on the raw file.

## Dataset
`data/sales_data_raw.csv`

## Tasks
1. Import the raw CSV, open **Transform Data** (Power Query Editor).
2. Build these steps in order (each becomes an "Applied Step"):
   - Remove duplicate rows based on `OrderID`
   - Trim/Clean text columns (`Region`, `Channel`, `SalesRep`)
   - Standardize `Region` casing (Capitalize Each Word)
   - Parse `OrderDate`: handle mixed date formats — split into a
     consistent `Date` type column (hint: you may need a custom column
     with conditional logic based on string length/pattern before
     converting type)
   - Replace blanks in `Region`/`SalesRep` with `"Unknown"`
   - Remove rows where `Quantity` AND `UnitPrice` are both blank
     (unrecoverable rows)
   - Add a calculated column `Revenue_Check` = `Quantity * UnitPrice`,
     compare against existing `Revenue` to catch mismatches
3. Rename the query to `Sales_Cleaned`.
4. Close & Apply.

## Deliverable
`day09_solved.pbix` with a fully documented `Sales_Cleaned` query
(applied steps visible = your audit trail).
