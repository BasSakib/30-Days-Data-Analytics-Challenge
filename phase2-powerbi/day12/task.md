# Day 12 — Visual Storytelling: Charts, Maps, KPIs

## Goal
Turn your measures into a real story, not just a grid of visuals.

## Tasks
1. New report page: "Sales Story".
2. Add:
   - **KPI visual**: Total Revenue vs target (set target 10% above current)
   - **Line chart**: `Total Revenue` by `Dim_Date[MonthName]`, sorted by
     `Dim_Date[Month]`
   - **Map visual**: Revenue by `Region` (use Region as location — if
     Power BI can't geo-resolve fictional region names, use a filled
     bar chart instead and note why)
   - **Donut chart**: Revenue by `Category`
   - **Bar chart**: Top 10 `SalesRep` by `Total Revenue`
3. Apply a consistent color theme (View → Themes) across all visuals.
4. Add a text box at the top summarizing the single biggest insight in
   one sentence (e.g., "Electronics drives 38% of revenue, led by North region").

## Deliverable
`day12_solved.pbix` with a "Sales Story" page telling a clear narrative.
