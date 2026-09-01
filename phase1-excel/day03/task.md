# Day 03 — Dynamic Lookups (XLOOKUP & VLOOKUP)

## Goal
Practice pulling data across tables using lookup functions — the most
used Excel skill in real analyst work.

## Setup
1. Create a small reference table on a new sheet `ProductRef` with columns:
   `Product`, `Category` (you can pull unique values from the sales data),
   and add a new column `SupplierCode` — make up realistic codes like
   `SUP-001`, `SUP-002`, etc., one per unique product.

## Tasks
1. In the main sales table, add a column `SupplierCode` and use
   **XLOOKUP** to pull it from `ProductRef` based on `Product`.
2. Add a column `CategoryCheck` using **VLOOKUP** that re-confirms the
   `Category` value from `ProductRef` (should match the existing Category
   column — use this to sanity-check your reference table).
3. Use XLOOKUP with the `if_not_found` argument to return `"Unmapped"`
   for any product not found in `ProductRef` (test this by deliberately
   removing one product from the reference table).
4. Save as `day03_solved.xlsx`.

## Deliverable
`day03_solved.xlsx` with `ProductRef` sheet and two new lookup columns.
