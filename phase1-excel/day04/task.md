# Day 04 — Data Hygiene: Duplicates & Missing Values

## Goal
Clean the raw dataset properly — this is the exercise the raw file was
built for.

## Dataset
`data/sales_data_raw.csv` (has ~40 duplicate rows and missing values by design)

## Tasks
1. Import the raw CSV fresh into a new sheet.
2. Use **Conditional Formatting → Highlight Duplicate Values** on `OrderID`
   to visually confirm duplicates exist.
3. Use **Data → Remove Duplicates** (based on `OrderID`) and record how many
   rows were removed.
4. Identify missing values:
   - Use `COUNTBLANK` per column to quantify how many blanks exist in
     `Region`, `SalesRep`, `UnitPrice`, `Quantity`.
5. Handle the missing values:
   - `Region` / `SalesRep` blanks → fill with `"Unknown"`
   - `UnitPrice` blanks → fill with the **average UnitPrice for that Product**
     (use AVERAGEIF)
   - `Quantity` blanks → fill with `1` (documented assumption)
6. Standardize text casing in `Region` and `Channel` using `PROPER` and
   `TRIM` (wrap in a helper column, then paste values back over the original).
7. Save as `day04_solved.xlsx`, and note your cleaning decisions on a
   `CleaningLog` sheet.

## Deliverable
`day04_solved.xlsx` — cleaned table + `CleaningLog` sheet documenting every
decision (this log is a great thing to reference in interviews).
