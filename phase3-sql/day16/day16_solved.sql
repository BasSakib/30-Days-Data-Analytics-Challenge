-- =========================================================
-- Day 16 — Advanced Filtering: WHERE, AND, OR
-- =========================================================

-- 1. North region orders with Revenue > 500
SELECT *
FROM sales
WHERE Region = 'North' AND Revenue > 500;

-- 2. Orders from Online OR Distributor channels
SELECT *
FROM sales
WHERE Channel = 'Online' OR Channel = 'Distributor';

-- 3. Electronics orders, quantity >= 10, excluding South region
SELECT *
FROM sales
WHERE Category = 'Electronics'
  AND Quantity >= 10
  AND Region != 'South';

-- 4. Orders from a specific set of sales reps
SELECT *
FROM sales
WHERE SalesRep IN ('Tanvir Ahmed', 'Farzana Islam', 'Rakib Hasan');

-- 5. Orders placed in Q1 2024 (Jan 1 – Mar 31)
SELECT *
FROM sales
WHERE OrderDate BETWEEN '2024-01-01' AND '2024-03-31';

-- 6. Products containing the word "Chair"
SELECT *
FROM sales
WHERE Product LIKE '%Chair%';
