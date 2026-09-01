"""
Day 29 Capstone — Step 2: Python Analysis
Connects to the SQLite database built by capstone_clean.sql, pulls
sales_clean, runs a full analysis, and exports the final analysis-ready
CSV that feeds the Day 29 BI dashboard.

Run capstone_clean.sql against a SQLite db named capstone.db before
running this script (or adjust DB_PATH below).
"""
import sqlite3
import pandas as pd
import numpy as np

DB_PATH = "capstone.db"

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("SELECT * FROM sales_clean", conn)
conn.close()

# OrderDate arrives with mixed formats (YYYY-MM-DD, DD/MM/YYYY, MM-DD-YYYY)
# since the SQL cleaning step standardized text/casing but not dates.
df["OrderDate"] = pd.to_datetime(df["OrderDate"], format="mixed", dayfirst=False)
df["OrderMonth"] = df["OrderDate"].dt.to_period("M").astype(str)
df["OrderYear"] = df["OrderDate"].dt.year

# --- Feature: profit estimate ---
# Assumption carried over from Day 21: 30% margin on Electronics/Furniture,
# 15% margin on Grocery/Apparel/Stationery
df["EstimatedProfit"] = df.apply(
    lambda row: row["Revenue"] * (0.30 if row["Category"] in ("Electronics", "Furniture") else 0.15),
    axis=1,
).round(2)

# --- Feature: customer/order segment by order size ---
df["OrderSegment"] = pd.cut(
    df["Quantity"], bins=[0, 4, 14, float("inf")], labels=["Small", "Medium", "Large"]
)

# --- Analysis ---
print("=" * 60)
print("TOP PRODUCTS BY REVENUE")
print("=" * 60)
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10)
print(top_products.round(2))

print("\n" + "=" * 60)
print("REGIONAL PERFORMANCE")
print("=" * 60)
regional = df.groupby("Region").agg(
    total_revenue=("Revenue", "sum"),
    total_orders=("OrderID", "count"),
    avg_order_value=("Revenue", "mean"),
    estimated_profit=("EstimatedProfit", "sum"),
).sort_values("total_revenue", ascending=False)
print(regional.round(2))

print("\n" + "=" * 60)
print("MONTHLY TREND")
print("=" * 60)
monthly = df.groupby("OrderMonth")["Revenue"].sum()
print(monthly.round(2))

# Year-over-year growth (2025 vs 2024)
rev_2024 = df[df["OrderYear"] == 2024]["Revenue"].sum()
rev_2025 = df[df["OrderYear"] == 2025]["Revenue"].sum()
yoy_growth = (rev_2025 - rev_2024) / rev_2024 * 100 if rev_2024 else np.nan
print(f"\n2024 Revenue: ${rev_2024:,.2f}")
print(f"2025 Revenue: ${rev_2025:,.2f}")
print(f"YoY Growth: {yoy_growth:.1f}%")

print("\n" + "=" * 60)
print("ORDER SEGMENT BREAKDOWN")
print("=" * 60)
print(df["OrderSegment"].value_counts())

# --- Export final analysis-ready CSV for the BI dashboard ---
output_path = "../../data/sales_data_capstone_final.csv"
df.to_csv(output_path, index=False)
print(f"\nFinal capstone dataset saved to {output_path}")
print(f"Shape: {df.shape}")
