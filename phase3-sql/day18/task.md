# Day 18 — Table Integration: JOINs

## Goal
Practice joins by splitting the flat sales table into normalized pieces
and rejoining them.

## Setup
1. Create two small lookup tables:
   - `sales_reps (rep_id INTEGER PRIMARY KEY, rep_name TEXT, region TEXT)`
   - `products (product_id INTEGER PRIMARY KEY, product_name TEXT, category TEXT, unit_cost REAL)`
   Populate with distinct values pulled from the sales data (make up
   `unit_cost` as ~70% of average UnitPrice per product).

## Tasks
1. `INNER JOIN` sales to `products` on product name — return
   Revenue alongside `unit_cost`, and compute estimated profit
   (`Revenue - Quantity * unit_cost`).
2. `LEFT JOIN` sales to `sales_reps` — confirm every sale has a matching
   rep (count any NULLs).
3. A 3-table join: sales + products + sales_reps together, selecting
   OrderID, rep_name, product_name, category, Revenue.
4. Demonstrate the difference: run the same join as `INNER JOIN` vs
   `LEFT JOIN` where you've deliberately removed one product from the
   `products` table, and compare row counts.

## Deliverable
`day18_solved.sql` — table creation, population, and all join queries.
