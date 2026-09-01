# Day 15 — Database Basics: CREATE TABLE & SELECT

## Goal
Load the sales data into a real SQL database and write your first queries.

## Setup
Solved file uses **SQLite** syntax (works with PostgreSQL/MySQL with
minor tweaks) so you can run it with zero server setup.

## Tasks
1. Write `CREATE TABLE sales (...)` matching the columns in
   `data/sales_data_clean.csv` with appropriate types
   (`OrderID INTEGER PRIMARY KEY`, `OrderDate TEXT` or `DATE`, etc.)
2. Load the CSV into the table (`.import` in sqlite3 CLI, or `COPY` in
   Postgres — document whichever you use).
3. Write basic SELECT queries:
   - All columns, first 20 rows
   - Only `OrderDate`, `Region`, `Revenue`, ordered by `Revenue` descending
   - `SELECT DISTINCT Region FROM sales`
   - `SELECT COUNT(*) FROM sales`

## Deliverable
`day15_solved.sql` containing the CREATE TABLE statement and all queries,
each with a comment explaining what it returns.
