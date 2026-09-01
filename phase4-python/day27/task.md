# Day 27 — Integration: Python + SQL

## Goal
Connect Python directly to a SQL database and query it with Pandas.

## Tasks
1. Use `sqlite3` (or `sqlalchemy`) to create/connect to a local database file.
2. Load your cleaned DataFrame into a `sales` table using
   `df.to_sql('sales', conn, if_exists='replace')`.
3. Run a SQL query directly from Python using `pd.read_sql()`:
   - Reuse one of your Day 21 business-question queries
   - Confirm the result matches what you got doing it in Pandas
4. Write a small reusable function `run_query(sql: str) -> pd.DataFrame`
   that wraps the connection + read_sql, so it can be reused across days.
5. Demonstrate the automation angle: write a function that takes a
   Region name as a parameter and returns that region's summary stats
   (revenue, orders, avg order value) — both as a raw SQL string built
   with parameters (avoid SQL injection — use `?` placeholders) and
   printed as a clean report.

## Deliverable
`day27_solved.py` with the DB connection, `run_query()` helper, and the
parameterized region-summary function.
