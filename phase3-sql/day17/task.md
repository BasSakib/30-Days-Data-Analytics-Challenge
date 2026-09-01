# Day 17 — Data Aggregation: GROUP BY Revenue Summaries

## Goal
Summarize data the way a stakeholder would ask for it.

## Tasks
Write queries for:
1. Total Revenue and Total Orders per `Region`.
2. Average `Revenue` per `Category`, sorted highest to lowest.
3. Total `Quantity` sold per `Product`, only showing products with
   total quantity > 500 (use `HAVING`).
4. Monthly revenue trend: `Revenue` summed by year-month
   (use `strftime('%Y-%m', OrderDate)` in SQLite).
5. Revenue per `SalesRep` per `Region` (two-column GROUP BY).

## Deliverable
`day17_solved.sql` with all 5 queries, commented, plus a one-line note
under each about what business question it answers.
