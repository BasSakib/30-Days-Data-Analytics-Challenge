# Day 23 — Data Manipulation: Filter, Sort, Select

## Goal
Practice core row/column selection and manipulation.

## Tasks
1. Select only orders where `Region == 'North'` and `Revenue > 500`.
2. Select only the columns `OrderID`, `Product`, `Revenue`.
3. Sort the full dataset by `Revenue` descending, show top 10.
4. Create a new column `OrderSize` using `pd.cut()` or a custom function
   on `Quantity` (bins: Small < 5, Medium 5–14, Large >= 15).
5. Use `.query()` to replicate one of the filters above with different syntax.
6. Use boolean indexing to find all orders with `Category == 'Electronics'`
   AND `Channel == 'Online'`.

## Deliverable
`day23_solved.py` with all steps and printed/exported results.
