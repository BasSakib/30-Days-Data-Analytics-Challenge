"""
Day 28 — Full EDA Report & Insights (Phase 4 Capstone)
Combines cleaning (Day 24), analysis (Day 25), visuals (Day 26),
and SQL integration (Day 27) into one organized pipeline.
"""
import os
import sqlite3
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("charts", exist_ok=True)

# =====================================================================
# SECTION 1: LOAD & CLEAN (Day 22 + Day 24)
# =====================================================================
print("SECTION 1: Load & Clean")
print("-" * 60)

raw = pd.read_csv("../../data/sales_data_raw.csv")
print(f"Raw rows: {len(raw)}")

df = raw.drop_duplicates(subset=["OrderID"], keep="first").copy()
df["Region"] = df["Region"].astype(str).str.strip().str.title().replace("Nan", "Unknown")
df["Channel"] = df["Channel"].astype(str).str.strip().str.title()
df["SalesRep"] = df["SalesRep"].fillna("Unknown")
df["Region"] = df["Region"].fillna("Unknown")


def parse_mixed_date(s):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return pd.to_datetime(s, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT


df["OrderDate"] = df["OrderDate"].apply(parse_mixed_date)
df["UnitPrice"] = df["UnitPrice"].fillna(df.groupby("Product")["UnitPrice"].transform("mean")).round(2)
df["Quantity"] = df["Quantity"].fillna(1)
df["OrderMonth"] = df["OrderDate"].dt.month
df["OrderYear"] = df["OrderDate"].dt.year
df["OrderWeekday"] = df["OrderDate"].dt.day_name()
df["YearMonth"] = df["OrderDate"].dt.to_period("M").astype(str)

print(f"Cleaned rows: {len(df)}")
print(f"Remaining missing values: {df.isnull().sum().sum()}\n")

# =====================================================================
# SECTION 2: ANALYSIS (Day 25)
# =====================================================================
print("SECTION 2: Analysis")
print("-" * 60)

rev_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
rev_by_category = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
aov_by_channel = df.groupby("Channel")["Revenue"].mean().sort_values(ascending=False)
rev_by_month = df.groupby("YearMonth")["Revenue"].sum()

top_region = rev_by_region.index[0]
top_category = rev_by_category.index[0]
top_channel = aov_by_channel.index[0]

print(f"Top region: {top_region} (${rev_by_region.iloc[0]:,.0f})")
print(f"Top category: {top_category} (${rev_by_category.iloc[0]:,.0f})")
print(f"Highest AOV channel: {top_channel} (${aov_by_channel.iloc[0]:,.2f})\n")

# =====================================================================
# SECTION 3: VISUALS (Day 26)
# =====================================================================
print("SECTION 3: Visuals")
print("-" * 60)

plt.figure(figsize=(8, 5))
ax = sns.barplot(x=rev_by_region.index, y=rev_by_region.values,
                  hue=rev_by_region.index, palette="Blues_d", legend=False)
ax.set_title("Total Revenue by Region", fontsize=14, fontweight="bold")
ax.set_ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("charts/revenue_by_region.png", dpi=150)
plt.close()

plt.figure(figsize=(10, 5))
ax = sns.lineplot(x=rev_by_month.index, y=rev_by_month.values, marker="o")
ax.set_title("Monthly Revenue Trend", fontsize=14, fontweight="bold")
ax.set_ylabel("Revenue ($)")
plt.xticks(rotation=60, ha="right", fontsize=8)
plt.tight_layout()
plt.savefig("charts/monthly_revenue_trend.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
ax = sns.boxplot(data=df, x="Category", y="Revenue", hue="Category",
                  palette="Set2", legend=False)
ax.set_title("Revenue Distribution by Category", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("charts/revenue_by_category_box.png", dpi=150)
plt.close()

print("Saved 3 summary charts to charts/\n")

# =====================================================================
# SECTION 4: SQL INTEGRATION (Day 27)
# =====================================================================
print("SECTION 4: SQL Integration")
print("-" * 60)

conn = sqlite3.connect("sales_day28.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

top5_sql = pd.read_sql(
    "SELECT Product, SUM(Revenue) as total_revenue FROM sales "
    "GROUP BY Product ORDER BY total_revenue DESC LIMIT 5",
    conn,
)
print("Top 5 products (via SQL query):")
print(top5_sql)
conn.close()

# =====================================================================
# SECTION 5: EXECUTIVE SUMMARY
# =====================================================================
summary_text = f"""
EXECUTIVE SUMMARY
==================
This report covers {len(df):,} cleaned sales orders spanning 2024-2025 across
5 regions, 5 product categories, and 4 sales channels. The raw export required
deduplication, text standardization, mixed-date parsing, and missing-value
imputation before analysis (see Section 1).

Top 3 Insights:
1. {top_region} is the leading region by revenue at ${rev_by_region.iloc[0]:,.0f},
   outperforming every other region.
2. {top_category} is the top revenue-generating category at
   ${rev_by_category.iloc[0]:,.0f}, driven by higher-ticket items like laptops
   and sofas rather than sheer order volume.
3. The {top_channel} channel produces the highest average order value
   (${aov_by_channel.iloc[0]:,.2f}), suggesting it's where larger or bulk
   purchases concentrate.

Recommendation: Prioritize {top_category} inventory and marketing spend in
{top_region}, and investigate what drives larger basket sizes on the
{top_channel} channel to replicate that pattern elsewhere.
"""
print(summary_text)

with open("day28_eda_report.md", "w") as f:
    f.write("# Day 28 — Full EDA Report\n\n")
    f.write(summary_text.replace("EXECUTIVE SUMMARY\n==================\n", ""))
    f.write("\n## Charts\n")
    f.write("- `charts/revenue_by_region.png` — Total revenue by region\n")
    f.write("- `charts/monthly_revenue_trend.png` — Revenue trend over time\n")
    f.write("- `charts/revenue_by_category_box.png` — Revenue spread by category, with outliers\n")

print("\nSaved day28_eda_report.md")
