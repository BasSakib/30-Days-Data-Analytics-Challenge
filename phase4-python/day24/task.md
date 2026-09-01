# Day 24 — Feature Engineering: GroupBy, Merge, Missing Values

## Goal
Do the real cleaning + feature engineering pass in Pandas.

## Dataset
`data/sales_data_raw.csv`

## Tasks
1. **Clean**:
   - Drop exact duplicate rows (`.drop_duplicates()`)
   - Standardize `Region`/`Channel` text: `.str.strip().str.title()`
   - Parse `OrderDate` with mixed formats using `pd.to_datetime(..., format='mixed')`
     or a custom parser function
   - Fill missing `Region`/`SalesRep` with `"Unknown"`
   - Fill missing `UnitPrice` with the mean UnitPrice **per Product**
     (`groupby('Product')['UnitPrice'].transform('mean')`)
   - Fill missing `Quantity` with 1
2. **Feature engineer**:
   - Add `OrderMonth`, `OrderYear`, `OrderWeekday` from `OrderDate`
   - Add `RevenueCheck = Quantity * UnitPrice` and flag rows where it
     doesn't match the original `Revenue` column (>1% difference)
3. **Merge**: create a small `region_targets` DataFrame (Region, monthly
   target revenue — made up), merge it onto a monthly-region summary,
   and compute `% of target achieved`.
4. Save the cleaned result to `data/sales_data_python_cleaned.csv`.

## Deliverable
`day24_solved.py` with the full cleaning + feature engineering pipeline.
