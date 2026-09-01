# Day 20 — Performance Tuning: Indexes

## Goal
Understand how indexes affect query performance, and when to use them.

## Tasks
1. Run `EXPLAIN QUERY PLAN` (SQLite) on a filter query
   (`WHERE Region = 'North'`) before adding any index — note the plan
   (likely a full table scan).
2. Create an index: `CREATE INDEX idx_region ON sales(Region);`
3. Re-run the same `EXPLAIN QUERY PLAN` and compare — note the difference.
4. Create a composite index on `(Region, Category)` and test a query
   filtering on both columns.
5. Write a short note (in comments) on trade-offs: indexes speed up reads
   but slow down writes and use extra storage — when would you NOT
   want to index a column? (e.g., low-cardinality columns, write-heavy tables)

## Deliverable
`day20_solved.sql` with index creation statements, EXPLAIN outputs as
comments, and your written trade-off notes.
