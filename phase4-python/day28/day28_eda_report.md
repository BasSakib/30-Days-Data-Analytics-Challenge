# Day 28 — Full EDA Report


This report covers 3,000 cleaned sales orders spanning 2024-2025 across
5 regions, 5 product categories, and 4 sales channels. The raw export required
deduplication, text standardization, mixed-date parsing, and missing-value
imputation before analysis (see Section 1).

Top 3 Insights:
1. South is the leading region by revenue at $1,010,836,
   outperforming every other region.
2. Electronics is the top revenue-generating category at
   $2,528,145, driven by higher-ticket items like laptops
   and sofas rather than sheer order volume.
3. The Online channel produces the highest average order value
   ($1,877.07), suggesting it's where larger or bulk
   purchases concentrate.

Recommendation: Prioritize Electronics inventory and marketing spend in
South, and investigate what drives larger basket sizes on the
Online channel to replicate that pattern elsewhere.

## Charts
- `charts/revenue_by_region.png` — Total revenue by region
- `charts/monthly_revenue_trend.png` — Revenue trend over time
- `charts/revenue_by_category_box.png` — Revenue spread by category, with outliers
