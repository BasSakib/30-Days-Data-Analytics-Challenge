# Day 16 — Advanced Filtering: WHERE, AND, OR

## Goal
Practice precise filtering logic.

## Tasks
Write queries for:
1. All orders from `Region = 'North'` with `Revenue > 500`.
2. All orders where `Channel = 'Online'` OR `Channel = 'Distributor'`.
3. All orders in `Category = 'Electronics'` AND `Quantity >= 10`
   AND `Region != 'South'`.
4. All orders where `SalesRep` is one of a specific list of 3 reps
   (use `IN`).
5. All orders where `OrderDate` falls in Q1 2024 (use `BETWEEN` or
   date functions).
6. All orders where `Product` contains the word "Chair" (use `LIKE`).

## Deliverable
`day16_solved.sql` with all 6 queries, commented.
