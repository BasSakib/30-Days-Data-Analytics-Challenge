-- =========================================================
-- Day 15 — Database Basics: CREATE TABLE & SELECT
-- Dialect: SQLite (portable to PostgreSQL/MySQL with minor tweaks,
-- noted inline where relevant)
-- =========================================================

-- 1. Create the sales table
-- In PostgreSQL, INTEGER PRIMARY KEY works the same; in MySQL use
-- INT PRIMARY KEY AUTO_INCREMENT if you want auto-numbering.
CREATE TABLE sales (
    OrderID       INTEGER PRIMARY KEY,
    OrderDate     TEXT,       -- stored as ISO text (YYYY-MM-DD) for SQLite;
                              -- use DATE type in PostgreSQL/MySQL
    Region        TEXT,
    SalesRep      TEXT,
    Category      TEXT,
    Product       TEXT,
    Channel       TEXT,
    PaymentMethod TEXT,
    Quantity      INTEGER,
    UnitPrice     REAL,
    Revenue       REAL
);

-- 2. Load the CSV into the table
-- sqlite3 CLI:
--   sqlite3 sales.db
--   .mode csv
--   .import --skip 1 data/sales_data_clean.csv sales
--
-- PostgreSQL equivalent:
--   COPY sales FROM '/path/to/sales_data_clean.csv' WITH (FORMAT csv, HEADER true);

-- 3. Basic SELECT queries

-- All columns, first 20 rows
SELECT *
FROM sales
LIMIT 20;

-- Only OrderDate, Region, Revenue, ordered by Revenue descending
SELECT OrderDate, Region, Revenue
FROM sales
ORDER BY Revenue DESC;

-- Distinct regions in the dataset
SELECT DISTINCT Region
FROM sales;

-- Total row count
SELECT COUNT(*) AS total_orders
FROM sales;
