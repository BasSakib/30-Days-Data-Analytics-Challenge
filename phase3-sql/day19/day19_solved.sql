-- =========================================================
-- Day 19 — Window Functions: RANK & ROW_NUMBER
-- =========================================================

-- 1. Rank SalesReps by total revenue
SELECT
    SalesRep,
    SUM(Revenue) AS total_revenue,
    RANK() OVER (ORDER BY SUM(Revenue) DESC) AS revenue_rank
FROM sales
GROUP BY SalesRep
ORDER BY revenue_rank;

-- 2. Within each Region, rank products by total revenue
SELECT
    Region,
    Product,
    SUM(Revenue) AS total_revenue,
    RANK() OVER (PARTITION BY Region ORDER BY SUM(Revenue) DESC) AS rank_in_region
FROM sales
GROUP BY Region, Product
ORDER BY Region, rank_in_region;

-- 3. Highest-revenue single order per Region (ROW_NUMBER approach)
WITH ranked_orders AS (
    SELECT
        Region,
        OrderID,
        Revenue,
        ROW_NUMBER() OVER (PARTITION BY Region ORDER BY Revenue DESC) AS rn
    FROM sales
)
SELECT Region, OrderID, Revenue
FROM ranked_orders
WHERE rn = 1;

-- 4. Month-over-month comparison using LAG
WITH monthly AS (
    SELECT
        strftime('%Y-%m', OrderDate) AS year_month,
        SUM(Revenue) AS monthly_revenue
    FROM sales
    GROUP BY year_month
)
SELECT
    year_month,
    monthly_revenue,
    LAG(monthly_revenue) OVER (ORDER BY year_month) AS prev_month_revenue,
    monthly_revenue - LAG(monthly_revenue) OVER (ORDER BY year_month) AS mom_change
FROM monthly
ORDER BY year_month;

-- 5. Running total of revenue by date
SELECT
    OrderDate,
    Revenue,
    SUM(Revenue) OVER (ORDER BY OrderDate) AS running_total_revenue
FROM sales
ORDER BY OrderDate
LIMIT 50;
