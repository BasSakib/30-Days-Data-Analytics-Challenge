"""
Day 26 — Scientific Visualization: Matplotlib & Seaborn
Dataset: sales_data_python_cleaned.csv (from Day 24)
Outputs: 5 PNG charts saved to charts/
"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # non-interactive backend, safe for headless runs
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../../data/sales_data_python_cleaned.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["YearMonth"] = df["OrderDate"].dt.to_period("M").astype(str)

os.makedirs("charts", exist_ok=True)
sns.set_theme(style="whitegrid")

# 1. Bar chart — Total Revenue by Region
rev_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False).reset_index()
plt.figure(figsize=(8, 5))
ax = sns.barplot(data=rev_by_region, x="Region", y="Revenue", hue="Region",
                  palette="Blues_d", legend=False)
ax.set_title("Total Revenue by Region", fontsize=14, fontweight="bold")
ax.set_xlabel("Region")
ax.set_ylabel("Total Revenue ($)")
ax.yaxis.set_major_formatter(lambda x, pos: f"${x:,.0f}")
plt.tight_layout()
plt.savefig("charts/01_revenue_by_region.png", dpi=150)
plt.close()

# 2. Line chart — Monthly revenue trend
rev_by_month = df.groupby("YearMonth")["Revenue"].sum().reset_index()
plt.figure(figsize=(11, 5))
ax = sns.lineplot(data=rev_by_month, x="YearMonth", y="Revenue", marker="o")
ax.set_title("Monthly Revenue Trend", fontsize=14, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Total Revenue ($)")
plt.xticks(rotation=60, ha="right", fontsize=8)
plt.tight_layout()
plt.savefig("charts/02_monthly_revenue_trend.png", dpi=150)
plt.close()

# 3. Box plot — Revenue distribution by Category
plt.figure(figsize=(9, 5))
ax = sns.boxplot(data=df, x="Category", y="Revenue", hue="Category",
                  palette="Set2", legend=False)
ax.set_title("Revenue Distribution by Category", fontsize=14, fontweight="bold")
ax.set_xlabel("Category")
ax.set_ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("charts/03_revenue_boxplot_by_category.png", dpi=150)
plt.close()

# 4. Heatmap — correlation matrix
corr = df[["Quantity", "UnitPrice", "Revenue"]].corr()
plt.figure(figsize=(6, 5))
ax = sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", square=True)
ax.set_title("Correlation Matrix", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("charts/04_correlation_heatmap.png", dpi=150)
plt.close()

# 5. Histogram — Quantity distribution with KDE overlay
plt.figure(figsize=(8, 5))
ax = sns.histplot(data=df, x="Quantity", bins=25, kde=True, color="steelblue")
ax.set_title("Distribution of Order Quantity", fontsize=14, fontweight="bold")
ax.set_xlabel("Quantity")
ax.set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("charts/05_quantity_histogram.png", dpi=150)
plt.close()

print("Saved 5 charts to charts/:")
for f in sorted(os.listdir("charts")):
    print(" -", f)
