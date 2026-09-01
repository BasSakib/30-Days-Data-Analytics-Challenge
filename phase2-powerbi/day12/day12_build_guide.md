# Day 12 — Visual Storytelling — Solution Build Guide

## Page setup
New page, rename to **"Sales Story"**.

## Text box (top of page)
> "Electronics drives the largest share of revenue, led by strong Laptop
> and Smartphone sales concentrated in the South region."
(Swap in your own actual top finding once you've built the visuals below —
this is illustrative based on the shared dataset's typical distribution.)

## Visual 1 — KPI visual
- Visualizations pane → KPI
- Indicator: `[Total Revenue]`
- Trend axis: `Dim_Date[MonthName]`
- Target: create a quick measure `Revenue Target = [Total Revenue] * 1.1`
  and set it as the Target value

## Visual 2 — Line chart
- Axis: `Dim_Date[MonthName]` (sort by `Dim_Date[Month]` — click the visual,
  ⋯ menu → Sort by → Month, ascending)
- Values: `[Total Revenue]`

## Visual 3 — Map (or filled bar chart fallback)
- Try Map visual first: Location = `Region`
- If Power BI can't geo-resolve the fictional region names (North/South/
  East/West/Central are generic — it may still geocode them loosely, or
  fail entirely) → switch to a horizontal **Filled Bar Chart**:
  Axis = `Region`, Values = `[Total Revenue]`
- Either way, this visual answers: "where is revenue concentrated?"

## Visual 4 — Donut chart
- Legend: `Dim_Product[Category]`
- Values: `[Total Revenue]`

## Visual 5 — Bar chart
- Axis: `SalesRep`
- Values: `[Total Revenue]`
- Filter pane → Visual level filter → Top N → Top 10 by `[Total Revenue]`

## Theme
View tab → Themes → pick one built-in theme (e.g. "Executive") and apply
to the whole report so all 5 visuals share one consistent palette.
