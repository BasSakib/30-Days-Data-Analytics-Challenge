-- =========================================================
-- Day 20 — Performance Tuning: Indexes
-- =========================================================

-- 1. Check the query plan BEFORE adding an index
EXPLAIN QUERY PLAN
SELECT * FROM sales WHERE Region = 'North';
-- Expected output (before index): SCAN sales (older SQLite: "SCAN TABLE sales")
-- -> SQLite must read every row to check the Region column (full table scan).

-- 2. Create an index on Region
CREATE INDEX idx_region ON sales(Region);

-- 3. Re-run the same EXPLAIN QUERY PLAN
EXPLAIN QUERY PLAN
SELECT * FROM sales WHERE Region = 'North';
-- Expected output (after index): SEARCH TABLE sales USING INDEX idx_region (Region=?)
-- -> SQLite can jump directly to matching rows instead of scanning the whole table.

-- 4. Composite index on (Region, Category)
CREATE INDEX idx_region_category ON sales(Region, Category);

EXPLAIN QUERY PLAN
SELECT * FROM sales WHERE Region = 'North' AND Category = 'Electronics';
-- Expected: SEARCH TABLE sales USING INDEX idx_region_category (Region=? AND Category=?)
-- -> a composite index serves queries filtering on the leading column(s) together;
--    it also still helps a query filtering on Region alone.

-- 5. Trade-off notes
-- Indexes speed up SELECT/WHERE/JOIN/ORDER BY on the indexed column(s), but:
--   a) Every INSERT/UPDATE/DELETE now also has to update the index, so
--      write-heavy tables (e.g. a high-frequency logging table) pay a
--      real cost for every index added.
--   b) Each index consumes additional disk space — on a very large table,
--      several indexes can roughly double storage needs.
--   c) Low-cardinality columns (few distinct values, e.g. a boolean flag
--      or a column that's 95% one value) usually don't benefit much from
--      indexing — the query planner may still choose a full scan because
--      the index doesn't narrow the search enough to be worth using.
--   d) Rule of thumb: index columns used often in WHERE, JOIN ON, or
--      ORDER BY clauses on large tables; avoid over-indexing small tables
--      or columns that are rarely filtered on.
