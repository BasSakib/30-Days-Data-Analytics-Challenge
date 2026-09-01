"""
Day 22 — Pandas Essentials: Load & Inspect
Dataset: sales_data_raw.csv (intentionally messy)
"""
import pandas as pd

df = pd.read_csv("../../data/sales_data_raw.csv")

print("=" * 60)
print("SHAPE")
print("=" * 60)
print(df.shape)

print("\n" + "=" * 60)
print("INFO")
print("=" * 60)
df.info()

print("\n" + "=" * 60)
print("HEAD")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("TAIL")
print("=" * 60)
print(df.tail())

print("\n" + "=" * 60)
print("DESCRIBE (numeric columns)")
print("=" * 60)
print(df.describe())

print("\n" + "=" * 60)
print("DTYPE CHECK — flags")
print("=" * 60)
print(df.dtypes)
print("-> OrderDate is 'object' (string), not datetime — needs parsing.")
print("-> UnitPrice/Quantity are 'object' or float with NaNs due to blanks in the raw export.")

print("\n" + "=" * 60)
print("MISSING VALUES PER COLUMN")
print("=" * 60)
missing = df.isnull().sum()
print(missing[missing > 0])

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)
dupe_count = df.duplicated().sum()
dupe_orderid_count = df.duplicated(subset=["OrderID"]).sum()
print(f"Exact duplicate rows: {dupe_count}")
print(f"Duplicate OrderID rows: {dupe_orderid_count}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
missing_cols = list(missing[missing > 0].index)
print(
    f"This dataset has {df.shape[0]} rows, {df.shape[1]} columns, "
    f"{dupe_orderid_count} duplicate OrderID rows, and missing values "
    f"concentrated in columns: {', '.join(missing_cols)}."
)
