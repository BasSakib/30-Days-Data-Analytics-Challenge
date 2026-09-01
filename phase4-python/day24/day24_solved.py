"""
Day 24 — Feature Engineering: GroupBy, Merge, Missing Values
Dataset: sales_data_raw.csv (messy) -> cleaned + feature-engineered output
"""
import pandas as pd
import numpy as np

df = pd.read_csv("../../data/sales_data_raw.csv")
print(f"Starting rows: {len(df)}")

# --- 1. CLEAN ---

# Drop exact duplicate rows
before = len(df)
df = df.drop_duplicates()
print(f"Dropped {before - len(df)} exact duplicate rows")

# Also drop duplicate OrderIDs (keep first occurrence) — the raw file
# has near-duplicate rows sharing the same OrderID
before = len(df)
df = df.drop_duplicates(subset=["OrderID"], keep="first")
print(f"Dropped {before - len(df)} duplicate OrderID rows")

# Standardize text columns
df["Region"] = df["Region"].astype(str).str.strip().str.title()
df["Region"] = df["Region"].replace({"Nan": np.nan, "": np.nan})
df["Channel"] = df["Channel"].astype(str).str.strip().str.title()

# Parse mixed date formats
def parse_mixed_date(s):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return pd.to_datetime(s, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT

df["OrderDate"] = df["OrderDate"].apply(parse_mixed_date)
print(f"Unparseable dates: {df['OrderDate'].isna().sum()}")

# Fill missing Region / SalesRep with "Unknown"
df["Region"] = df["Region"].fillna("Unknown")
df["SalesRep"] = df["SalesRep"].fillna("Unknown")

# Fill missing UnitPrice with the mean UnitPrice per Product
df["UnitPrice"] = df["UnitPrice"].fillna(
    df.groupby("Product")["UnitPrice"].transform("mean")
).round(2)

# Fill missing Quantity with 1
df["Quantity"] = df["Quantity"].fillna(1)

print(f"\nMissing values after cleaning:\n{df.isnull().sum()[df.isnull().sum() > 0]}")

# --- 2. FEATURE ENGINEER ---

df["OrderMonth"] = df["OrderDate"].dt.month
df["OrderYear"] = df["OrderDate"].dt.year
df["OrderWeekday"] = df["OrderDate"].dt.day_name()

df["RevenueCheck"] = df["Quantity"] * df["UnitPrice"]
df["RevenueMismatch"] = (
    (df["RevenueCheck"] - df["Revenue"]).abs() / df["Revenue"].replace(0, np.nan) > 0.01
)
mismatch_count = df["RevenueMismatch"].sum()
print(f"\nRows where computed Revenue differs from stated Revenue by >1%: {mismatch_count}")

# --- 3. MERGE ---

# Made-up monthly target revenue per region
region_targets = pd.DataFrame({
    "Region": ["North", "South", "East", "West", "Central", "Unknown"],
    "monthly_target": [60000, 62000, 58000, 59000, 55000, 20000],
})

monthly_region_summary = (
    df.groupby(["OrderYear", "OrderMonth", "Region"])["Revenue"]
    .sum()
    .reset_index()
    .rename(columns={"Revenue": "actual_revenue"})
)

merged = monthly_region_summary.merge(region_targets, on="Region", how="left")
merged["pct_of_target"] = (merged["actual_revenue"] / merged["monthly_target"] * 100).round(1)

print("\nSample of merged monthly region summary vs. target:")
print(merged.sort_values(["OrderYear", "OrderMonth"]).head(10))

# --- 4. SAVE ---

output_path = "../../data/sales_data_python_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"\nCleaned + feature-engineered data saved to {output_path}")
print(f"Final shape: {df.shape}")
