-- =========================================================
-- Day 17 — Data Aggregation: GROUP BY Revenue Summaries
-- =========================================================

-- 1. Total Revenue and Total Orders per Region
-- Business question: which regions drive the most revenue and volume?
SELECT
    Region,
    SUM(Revenue)   AS total_revenue,
    COUNT(*)       AS total_orders
FROM sales
GROUP BY Region
ORDER BY total_revenue DESC;

-- 2. Average Revenue per Category, sorted highest to lowest
-- Business question: which product category has the highest-value orders on average?
SELECT
    Category,
    AVG(Revenue) AS avg_revenue
FROM sales
GROUP BY Category
ORDER BY avg_revenue DESC;

-- 3. Total Quantity sold per Product, only products with total quantity > 500
-- Business question: which products are moving the highest unit volume?
SELECT
    Product,
    SUM(Quantity) AS total_quantity
FROM sales
GROUP BY Product
HAVING SUM(Quantity) > 500
ORDER BY total_quantity DESC;

-- 4. Monthly revenue trend (year-month)
-- Business question: is revenue trending up or down month over month?
SELECT
    strftime('%Y-%m', OrderDate) AS year_month,
    SUM(Revenue) AS monthly_revenue
FROM sales
GROUP BY year_month
ORDER BY year_month;

-- 5. Revenue per SalesRep per Region
-- Business question: how does each rep's performance vary by region
-- (useful for reps who cover more than one region)?
SELECT
    SalesRep,
    Region,
    SUM(Revenue) AS total_revenue
FROM sales
GROUP BY SalesRep, Region
ORDER BY SalesRep, total_revenue DESC;
