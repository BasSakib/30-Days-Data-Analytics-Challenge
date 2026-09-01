"""
Day 23 — Data Manipulation: Filter, Sort, Select
Dataset: sales_data_clean.csv
"""
import pandas as pd

df = pd.read_csv("../../data/sales_data_clean.csv")

# 1. Filter: North region, Revenue > 500
north_high_value = df[(df["Region"] == "North") & (df["Revenue"] > 500)]
print("1. North + Revenue > 500:", north_high_value.shape[0], "rows")
print(north_high_value.head(3), "\n")

# 2. Select specific columns
subset = df[["OrderID", "Product", "Revenue"]]
print("2. Selected columns:\n", subset.head(3), "\n")

# 3. Sort by Revenue descending, top 10
top10 = df.sort_values("Revenue", ascending=False).head(10)
print("3. Top 10 by Revenue:\n", top10[["OrderID", "Product", "Revenue"]], "\n")

# 4. New column OrderSize via pd.cut on Quantity
df["OrderSize"] = pd.cut(
    df["Quantity"],
    bins=[0, 4, 14, float("inf")],
    labels=["Small", "Medium", "Large"],
)
print("4. OrderSize distribution:\n", df["OrderSize"].value_counts(), "\n")

# 5. Same filter as #1, using .query() syntax instead
north_high_value_query = df.query("Region == 'North' and Revenue > 500")
assert len(north_high_value_query) == len(north_high_value), "Query result mismatch!"
print("5. .query() result matches boolean filter:", len(north_high_value_query), "rows\n")

# 6. Boolean indexing: Electronics + Online channel
electronics_online = df[(df["Category"] == "Electronics") & (df["Channel"] == "Online")]
print("6. Electronics + Online:", electronics_online.shape[0], "rows")
print(electronics_online.head(3))
