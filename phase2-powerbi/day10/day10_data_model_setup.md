# Day 10 — Data Modeling: Table Relationships — Solution

## Dim_Product (Power Query, New Blank Query or reference Sales_Cleaned)
```
let
    Source = Sales_Cleaned,
    Selected = Table.SelectColumns(Source, {"Product", "Category"}),
    Distinct = Table.Distinct(Selected)
in
    Distinct
```

## Dim_Region
```
let
    Source = Sales_Cleaned,
    Selected = Table.SelectColumns(Source, {"Region"}),
    Distinct = Table.Distinct(Selected)
in
    Distinct
```

## Dim_Date (DAX calculated table — Modeling tab > New Table)
```
Dim_Date =
VAR MinDate = MIN(Sales_Cleaned[OrderDate])
VAR MaxDate = MAX(Sales_Cleaned[OrderDate])
RETURN
ADDCOLUMNS(
    CALENDAR(MinDate, MaxDate),
    "Year", YEAR([Date]),
    "Month", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "Quarter", "Q" & FORMAT([Date], "Q")
)
```

## Relationships (Model view)
Drag to connect:
- `Sales_Cleaned[Product]` → `Dim_Product[Product]` — Many-to-one, single direction
- `Sales_Cleaned[Region]` → `Dim_Region[Region]` — Many-to-one, single direction
- `Sales_Cleaned[OrderDate]` → `Dim_Date[Date]` — Many-to-one, single direction

All three should render as **solid lines** in Model view (solid = active
relationship; dotted = inactive — only one active relationship is allowed
between two tables at a time). Cardinality should read "1" on the Dim
table side and "*" (many) on the Sales_Cleaned side.

## How to verify it worked
Build a quick bar chart: Axis = `Dim_Product[Category]`, Values =
`SUM(Sales_Cleaned[Revenue])`. If the chart populates correctly, the
Sales_Cleaned → Dim_Product relationship is working (Power BI can only
"see across" tables through an active relationship).
