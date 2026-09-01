# Day 11 — DAX Foundations: Monthly Sales Measures

## Goal
Write your first real DAX measures.

## Tasks
Create a new Measures table (or add to `Sales_Cleaned`) with:

1. `Total Revenue = SUM(Sales_Cleaned[Revenue])`
2. `Total Orders = DISTINCTCOUNT(Sales_Cleaned[OrderID])`
3. `Average Order Value = DIVIDE([Total Revenue], [Total Orders])`
4. `Total Quantity = SUM(Sales_Cleaned[Quantity])`
5. `Revenue LM (Last Month) = CALCULATE([Total Revenue], DATEADD(Dim_Date[Date], -1, MONTH))`
6. `Revenue MoM % = DIVIDE([Total Revenue] - [Revenue LM], [Revenue LM])`
7. `High Value Orders = CALCULATE([Total Orders], Sales_Cleaned[Revenue] > 500)`

Add all 7 measures as Cards on the Overview page to confirm they calculate
correctly.

## Deliverable
`day11_solved.pbix` with 7 working DAX measures visible as Card visuals.
