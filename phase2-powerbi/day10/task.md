# Day 10 — Data Modeling: Table Relationships

## Goal
Move from a single flat table to a small star schema.

## Tasks
1. In Power Query, create two new reference tables from `Sales_Cleaned`:
   - `Dim_Product` — unique `Product`, `Category` (Remove Duplicates on Product)
   - `Dim_Region` — unique `Region`
2. Create a `Dim_Date` table (Power Query → New Source → Blank Query,
   or DAX `CALENDAR()`) spanning your OrderDate min/max, with columns:
   `Date`, `Year`, `Month`, `MonthName`, `Quarter`.
3. In **Model view**, create relationships:
   - `Sales_Cleaned[Product]` → `Dim_Product[Product]` (many-to-one)
   - `Sales_Cleaned[Region]` → `Dim_Region[Region]` (many-to-one)
   - `Sales_Cleaned[OrderDate]` → `Dim_Date[Date]` (many-to-one)
4. Verify relationships are all single-direction, many-to-one, active
   (solid lines, not dotted).
5. Save as `day10_solved.pbix`.

## Deliverable
`day10_solved.pbix` with a working star schema visible in Model view.
