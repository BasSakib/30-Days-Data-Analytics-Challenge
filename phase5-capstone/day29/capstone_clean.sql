-- =========================================================
-- Day 29 Capstone — Step 1: SQL Cleaning
-- Loads sales_data_raw.csv into SQLite and produces sales_clean.
-- =========================================================

CREATE TABLE sales_raw (
    OrderID       INTEGER,
    OrderDate     TEXT,
    Region        TEXT,
    SalesRep      TEXT,
    Category      TEXT,
    Product       TEXT,
    Channel       TEXT,
    PaymentMethod TEXT,
    Quantity      REAL,
    UnitPrice     REAL,
    Revenue       REAL
);

-- Load via: sqlite3 capstone.db
--   .mode csv
--   .import --skip 1 data/sales_data_raw.csv sales_raw

-- Deduplicate: keep the first occurrence of each OrderID
CREATE TABLE sales_clean AS
SELECT *
FROM sales_raw
WHERE rowid IN (
    SELECT MIN(rowid)
    FROM sales_raw
    GROUP BY OrderID
);

-- Standardize Region/Channel casing and whitespace
UPDATE sales_clean
SET Region = TRIM(Region),
    Channel = TRIM(Channel);

-- SQLite has no built-in PROPER/INITCAP — normalize case for the known
-- categorical values directly (safe since Region/Channel are closed sets)
UPDATE sales_clean SET Region = 'North'   WHERE UPPER(Region) = 'NORTH';
UPDATE sales_clean SET Region = 'South'   WHERE UPPER(Region) = 'SOUTH';
UPDATE sales_clean SET Region = 'East'    WHERE UPPER(Region) = 'EAST';
UPDATE sales_clean SET Region = 'West'    WHERE UPPER(Region) = 'WEST';
UPDATE sales_clean SET Region = 'Central' WHERE UPPER(Region) = 'CENTRAL';

UPDATE sales_clean SET Channel = 'Online'        WHERE UPPER(Channel) = 'ONLINE';
UPDATE sales_clean SET Channel = 'Retail Store'  WHERE UPPER(Channel) = 'RETAIL STORE';
UPDATE sales_clean SET Channel = 'Distributor'   WHERE UPPER(Channel) = 'DISTRIBUTOR';
UPDATE sales_clean SET Channel = 'Wholesale'     WHERE UPPER(Channel) = 'WHOLESALE';

-- Fill missing Region / SalesRep with 'Unknown'
UPDATE sales_clean SET Region = 'Unknown' WHERE Region IS NULL OR Region = '';
UPDATE sales_clean SET SalesRep = 'Unknown' WHERE SalesRep IS NULL OR SalesRep = '';

-- Fill missing UnitPrice with the average UnitPrice for that Product
UPDATE sales_clean
SET UnitPrice = (
    SELECT AVG(UnitPrice) FROM sales_clean s2
    WHERE s2.Product = sales_clean.Product AND s2.UnitPrice IS NOT NULL
)
WHERE UnitPrice IS NULL;

-- Fill missing Quantity with 1
UPDATE sales_clean SET Quantity = 1 WHERE Quantity IS NULL;

-- Sanity check
SELECT COUNT(*) AS total_rows,
       SUM(CASE WHEN Region IS NULL THEN 1 ELSE 0 END) AS null_regions,
       SUM(CASE WHEN UnitPrice IS NULL THEN 1 ELSE 0 END) AS null_prices
FROM sales_clean;
