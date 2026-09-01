-- =========================================================
-- Day 18 — Table Integration: JOINs
-- =========================================================

-- --- Setup: create and populate lookup tables ---

CREATE TABLE sales_reps (
    rep_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    rep_name   TEXT UNIQUE,
    region     TEXT
);

INSERT INTO sales_reps (rep_name, region)
SELECT DISTINCT SalesRep,
       -- pick each rep's most common region as their "home" region
       (SELECT Region FROM sales s2
        WHERE s2.SalesRep = s1.SalesRep
        GROUP BY Region ORDER BY COUNT(*) DESC LIMIT 1)
FROM sales s1
WHERE SalesRep IS NOT NULL;

CREATE TABLE products (
    product_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT UNIQUE,
    category     TEXT,
    unit_cost    REAL
);

INSERT INTO products (product_name, category, unit_cost)
SELECT DISTINCT Product, Category,
       ROUND((SELECT AVG(UnitPrice) FROM sales s2 WHERE s2.Product = s1.Product) * 0.70, 2)
FROM sales s1;

-- --- Queries ---

-- 1. INNER JOIN sales to products -> Revenue alongside unit_cost, plus estimated profit
SELECT
    s.OrderID,
    s.Product,
    s.Quantity,
    s.Revenue,
    p.unit_cost,
    ROUND(s.Revenue - (s.Quantity * p.unit_cost), 2) AS estimated_profit
FROM sales s
INNER JOIN products p ON s.Product = p.product_name
LIMIT 20;

-- 2. LEFT JOIN sales to sales_reps -> confirm every sale has a matching rep
SELECT
    s.OrderID,
    s.SalesRep,
    r.rep_id
FROM sales s
LEFT JOIN sales_reps r ON s.SalesRep = r.rep_name
WHERE r.rep_id IS NULL;   -- should return 0 rows if every rep matches

-- 3. Three-table join: sales + products + sales_reps
SELECT
    s.OrderID,
    r.rep_name,
    p.product_name,
    p.category,
    s.Revenue
FROM sales s
INNER JOIN products p   ON s.Product = p.product_name
INNER JOIN sales_reps r ON s.SalesRep = r.rep_name
LIMIT 20;

-- 4. INNER vs LEFT JOIN comparison after removing one product from `products`
-- (run this block to see the difference in matched row counts)
DELETE FROM products WHERE product_name = 'Laptop';

SELECT 'INNER JOIN row count' AS label, COUNT(*) AS row_count
FROM sales s
INNER JOIN products p ON s.Product = p.product_name
UNION ALL
SELECT 'LEFT JOIN row count', COUNT(*)
FROM sales s
LEFT JOIN products p ON s.Product = p.product_name;
-- INNER JOIN drops every Laptop order; LEFT JOIN keeps them with NULL product columns.
