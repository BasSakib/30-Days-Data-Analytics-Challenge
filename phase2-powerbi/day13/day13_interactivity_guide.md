# Day 13 — Interactive Reports — Solution Build Guide

## Slicers (add to "Sales Story" page)
1. Visualizations pane → Slicer → field: `Dim_Date[Year]` → Format pane →
   Slicer settings → Style: **Tile** (renders as clickable buttons)
2. Slicer → field: `Region` → Style: **Dropdown**
3. Slicer → field: `Channel` → Style: **Dropdown**

## Cross-filtering
This is **on by default** in Power BI — clicking a slice in the Category
donut chart automatically filters every other visual on the page that
shares a relationship to `Category`. To confirm/adjust:
- Click the donut chart → Format tab → Edit Interactions → check that the
  line chart and Top 10 SalesRep chart show the "filter" icon (funnel),
  not "none".

## Drill-through page
1. Add a new page, rename to **"Region Detail"**
2. Drag `Region` into the **Drill through** filters well (Visualizations
   pane, bottom section)
3. Add to this page: a table of all raw order columns, plus 3-4 Card
   visuals reusing your Day 11 measures (`[Total Revenue]`, `[Total
   Orders]`, `[Average Order Value]`)
4. On "Sales Story", right-click any Region value in a visual → Drill
   Through → Region Detail

## Bookmarks
1. View tab → Bookmarks pane → "Add"
2. With no filters applied, click Add → rename to **"Full View"**
3. Apply the Channel slicer to "Online" only → click Add → rename to
   **"Online Channel Only"**
4. Insert → Buttons → Blank → add 2 buttons on the page → Format each
   button's Action: Type = Bookmark, Bookmark = the one you want it to
   jump to
5. Label the buttons "Full View" and "Online Only"
