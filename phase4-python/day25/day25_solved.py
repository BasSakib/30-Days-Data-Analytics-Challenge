"""
Day 25 — Exploratory Data Analysis (EDA)
Dataset: sales_data_python_cleaned.csv (from Day 24)
"""
import pandas as pd

df = pd.read_csv("../../data/sales_data_python_cleaned.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# --- 1. Revenue distribution ---
print("=" * 60)
print("REVENUE DISTRIBUTION")
print("=" * 60)
print(df["Revenue"].describe())
print(f"Skew: {df['Revenue'].skew():.3f}")

q1 = df["Revenue"].quantile(0.25)
q3 = df["Revenue"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df["Revenue"] < lower_bound) | (df["Revenue"] > upper_bound)]
print(f"IQR bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"Outlier orders (beyond 1.5xIQR): {len(outliers)} ({len(outliers)/len(df)*100:.1f}%)")

# --- 2. Correlation ---
print("\n" + "=" * 60)
print("CORRELATION MATRIX (numeric columns)")
print("=" * 60)
corr = df[["Quantity", "UnitPrice", "Revenue"]].corr()
print(corr)

# --- 3. Group-level patterns ---
print("\n" + "=" * 60)
print("REVENUE BY REGION")
print("=" * 60)
rev_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print(rev_by_region)

print("\n" + "=" * 60)
print("REVENUE BY CATEGORY")
print("=" * 60)
rev_by_category = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
print(rev_by_category)

print("\n" + "=" * 60)
print("AVERAGE ORDER VALUE BY CHANNEL")
print("=" * 60)
aov_by_channel = df.groupby("Channel")["Revenue"].mean().sort_values(ascending=False)
print(aov_by_channel.round(2))

# --- 4. Time patterns ---
print("\n" + "=" * 60)
print("REVENUE BY MONTH")
print("=" * 60)
df["YearMonth"] = df["OrderDate"].dt.to_period("M")
rev_by_month = df.groupby("YearMonth")["Revenue"].sum()
print(rev_by_month)

print("\n" + "=" * 60)
print("REVENUE BY WEEKDAY")
print("=" * 60)
rev_by_weekday = df.groupby("OrderWeekday")["Revenue"].sum().sort_values(ascending=False)
print(rev_by_weekday)

# --- 5. Findings ---
top_region = rev_by_region.index[0]
top_category = rev_by_category.index[0]
top_channel = aov_by_channel.index[0]
top_weekday = rev_by_weekday.index[0]

print("\n" + "=" * 60)
print("KEY FINDINGS")
print("=" * 60)
findings = [
    f"1. {top_region} is the top-revenue region at ${rev_by_region.iloc[0]:,.0f}, "
    f"roughly {(rev_by_region.iloc[0]/rev_by_region.iloc[-1] - 1)*100:.0f}% higher than "
    f"the lowest-performing region.",
    f"2. {top_category} drives the most total revenue (${rev_by_category.iloc[0]:,.0f}), "
    f"consistent with its higher average unit price relative to categories like Grocery or Stationery.",
    f"3. The {top_channel} channel has the highest average order value "
    f"(${aov_by_channel.iloc[0]:,.2f}), suggesting it attracts larger or bulk purchases.",
    f"4. Revenue outliers make up {len(outliers)/len(df)*100:.1f}% of orders — mostly "
    f"large-quantity Electronics/Furniture purchases, not data errors.",
    f"5. {top_weekday} generates the highest total revenue by weekday, worth considering "
    f"for promotional timing.",
]
for f in findings:
    print(f)
