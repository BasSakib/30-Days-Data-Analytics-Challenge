"""
Day 27 — Integration: Python + SQL
Connects to a local SQLite database and queries it with Pandas.
"""
import sqlite3
import pandas as pd

DB_PATH = "sales_day27.db"

# --- 1. Load cleaned data into SQLite ---
df = pd.read_csv("../../data/sales_data_python_cleaned.csv")
conn = sqlite3.connect(DB_PATH)
df.to_sql("sales", conn, if_exists="replace", index=False)
print(f"Loaded {len(df)} rows into '{DB_PATH}' -> table 'sales'")


# --- 2. Reusable query helper ---
def run_query(sql: str, params: tuple = ()) -> pd.DataFrame:
    """Run a SQL query against the sales database and return a DataFrame."""
    with sqlite3.connect(DB_PATH) as c:
        return pd.read_sql(sql, c, params=params)


# Reuse a Day 21-style business question: top 5 products by revenue
top_products_sql = """
    SELECT Product, SUM(Revenue) AS total_revenue
    FROM sales
    GROUP BY Product
    ORDER BY total_revenue DESC
    LIMIT 5
"""
top_products_sql_result = run_query(top_products_sql)
print("\nTop 5 products (via SQL):")
print(top_products_sql_result)

# Confirm it matches doing the same thing in pure Pandas
top_products_pandas = (
    df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)
)
print("\nTop 5 products (via Pandas):")
print(top_products_pandas)

sql_values = top_products_sql_result["total_revenue"].round(2).tolist()
pandas_values = top_products_pandas.round(2).tolist()
assert sql_values == pandas_values, "SQL and Pandas results don't match!"
print("\nSQL and Pandas results match. ✔")


# --- 3. Parameterized region summary function ---
def region_summary(region_name: str) -> pd.DataFrame:
    """
    Return revenue, order count, and average order value for a given region.
    Uses a parameterized query (?) to avoid SQL injection.
    """
    sql = """
        SELECT
            ? AS region,
            SUM(Revenue) AS total_revenue,
            COUNT(*) AS total_orders,
            ROUND(AVG(Revenue), 2) AS avg_order_value
        FROM sales
        WHERE Region = ?
    """
    return run_query(sql, params=(region_name, region_name))


print("\n" + "=" * 50)
print("REGION SUMMARY REPORTS")
print("=" * 50)
for region in ["North", "South", "East", "West", "Central"]:
    result = region_summary(region)
    row = result.iloc[0]
    print(
        f"\n{region}:\n"
        f"  Total Revenue:       ${row['total_revenue']:,.2f}\n"
        f"  Total Orders:        {row['total_orders']:,}\n"
        f"  Average Order Value: ${row['avg_order_value']:,.2f}"
    )

conn.close()
