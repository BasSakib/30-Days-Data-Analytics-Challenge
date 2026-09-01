# Day 19 — Window Functions: RANK & ROW_NUMBER

## Goal
Go beyond GROUP BY into row-level analytics.

## Tasks
1. Rank `SalesRep`s by total revenue using `RANK() OVER (ORDER BY SUM(Revenue) DESC)`.
2. Within each `Region`, rank products by total revenue using
   `RANK() OVER (PARTITION BY Region ORDER BY SUM(Revenue) DESC)`.
3. Use `ROW_NUMBER()` to find the single highest-revenue order per Region
   (partition by Region, order by Revenue desc, filter row_number = 1).
4. Use `LAG()` to compare each month's total revenue to the previous
   month's (partition isn't needed here — just ORDER BY month).
5. Calculate a running total of revenue by date using
   `SUM(Revenue) OVER (ORDER BY OrderDate)`.

## Deliverable
`day19_solved.sql` with all 5 window function queries, commented.
