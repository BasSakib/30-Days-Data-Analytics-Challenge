# Day 22 — Pandas Essentials: Load & Inspect

## Goal
Get comfortable with the core Pandas inspection toolkit.

## Dataset
`data/sales_data_raw.csv`

## Tasks
1. Load the CSV with `pd.read_csv()`.
2. Inspect: `.shape`, `.info()`, `.head()`, `.tail()`, `.describe()`.
3. Check data types per column — flag any that look wrong (e.g. is
   `OrderDate` a string instead of a datetime? Is `UnitPrice` object
   type because of blanks?).
4. Count missing values per column: `.isnull().sum()`.
5. Count duplicate rows: `.duplicated().sum()`.
6. Write a short printed summary: "This dataset has X rows, Y columns,
   Z duplicate rows, and missing values concentrated in columns: ..."

## Deliverable
`day22_solved.py` (or `.ipynb`) with all inspection steps and printed output.
