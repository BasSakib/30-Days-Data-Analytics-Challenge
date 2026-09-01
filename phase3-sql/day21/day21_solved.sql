-- =========================================================
-- Day 21 — Business Insights: Top Products & Peak-Time Trends
-- Phase 3 capstone — combines filtering, aggregation, joins, and
-- window functions from Days 15-20 into business-facing answers.
-- =========================================================

-- 1. Top 5 products by revenue, with % share of total revenue
-- Business question: which products should we prioritize for restocking/marketing?
WITH product_revenue AS (
    SELECT Product, SUM(Revenue) AS product_total
    FROM sales
    GROUP BY Product
),
grand_total AS (
    SELECT SUM(Revenue) AS total FROM sales
)
SELECT
    p.Product,
    p.product_total,
    ROUND(100.0 * p.product_total / g.total, 2) AS pct_of_total_revenue
FROM product_revenue p
CROSS JOIN grand_total g
ORDER BY p.product_total DESC
LIMIT 5;

-- 2. Which day of week generates the highest average revenue per order?
-- Business question: should staffing/promotions concentrate on specific weekdays?
SELECT
    CASE CAST(strftime('%w', OrderDate) AS INTEGER)
        WHEN 0 THEN 'Sunday'
        WHEN 1 THEN 'Monday'
        WHEN 2 THEN 'Tuesday'
        WHEN 3 THEN 'Wednesday'
        WHEN 4 THEN 'Thursday'
        WHEN 5 THEN 'Friday'
        WHEN 6 THEN 'Saturday'
    END AS weekday,
    ROUND(AVG(Revenue), 2) AS avg_revenue_per_order,
    COUNT(*) AS order_count
FROM sales
GROUP BY weekday
ORDER BY avg_revenue_per_order DESC;

-- 3. Most profitable Region + Category combination
-- Business question: where should we focus expansion investment?
-- Assumption: 30% margin on Electronics/Furniture, 15% on Grocery/Apparel/Stationery
SELECT
    Region,
    Category,
    SUM(Revenue) AS total_revenue,
    ROUND(SUM(Revenue) *
        CASE WHEN Category IN ('Electronics', 'Furniture') THEN 0.30 ELSE 0.15 END
    , 2) AS estimated_profit
FROM sales
GROUP BY Region, Category
ORDER BY estimated_profit DESC
LIMIT 10;

-- 4. "At risk" sales reps: most recent month's revenue below their own average
-- Business question: which reps may need coaching or support this quarter?
WITH rep_monthly AS (
    SELECT
        SalesRep,
        strftime('%Y-%m', OrderDate) AS year_month,
        SUM(Revenue) AS monthly_revenue
    FROM sales
    GROUP BY SalesRep, year_month
),
rep_avg AS (
    SELECT SalesRep, AVG(monthly_revenue) AS avg_monthly_revenue
    FROM rep_monthly
    GROUP BY SalesRep
),
rep_latest AS (
    SELECT SalesRep, monthly_revenue, year_month,
           ROW_NUMBER() OVER (PARTITION BY SalesRep ORDER BY year_month DESC) AS rn
    FROM rep_monthly
)
SELECT
    l.SalesRep,
    l.year_month AS latest_month,
    ROUND(l.monthly_revenue, 2) AS latest_month_revenue,
    ROUND(a.avg_monthly_revenue, 2) AS avg_monthly_revenue
FROM rep_latest l
JOIN rep_avg a ON l.SalesRep = a.SalesRep
WHERE l.rn = 1
  AND l.monthly_revenue < a.avg_monthly_revenue
ORDER BY (a.avg_monthly_revenue - l.monthly_revenue) DESC;

-- 5. Top 3 SalesReps per Region by revenue (window function + filter)
-- Business question: who are the regional top performers worth recognizing/studying?
WITH rep_region_revenue AS (
    SELECT
        Region,
        SalesRep,
        SUM(Revenue) AS total_revenue,
        RANK() OVER (PARTITION BY Region ORDER BY SUM(Revenue) DESC) AS region_rank
    FROM sales
    GROUP BY Region, SalesRep
)
SELECT Region, SalesRep, total_revenue, region_rank
FROM rep_region_revenue
WHERE region_rank <= 3
ORDER BY Region, region_rank;
