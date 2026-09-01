# Day 06 — Automation: Power Query & Goal Seek

## Goal
Use Power Query for repeatable cleaning, and Goal Seek for a business
what-if question.

## Part A — Power Query
1. Load `data/sales_data_raw.csv` via **Data → Get Data → From Text/CSV →
   Transform Data** (opens Power Query Editor).
2. In Power Query, replicate your Day 04 cleaning as repeatable steps:
   - Remove duplicate rows (by `OrderID`)
   - Trim and clean text in `Region` and `Channel`
   - Fill/replace blanks in `Region`/`SalesRep` with `"Unknown"`
   - Parse `OrderDate` into a consistent date type (handle the mixed formats)
3. Load the result into a new sheet `PQ_Cleaned`.
4. **Key point to demonstrate**: refresh the query and show it re-runs
   cleanly (add a screenshot or note in a `Notes` sheet).

## Part B — Goal Seek
1. On a `GoalSeek` sheet, set up: current Total Revenue (from your cleaned
   data), and a target Total Revenue that's 20% higher.
2. Use **Goal Seek** to answer: "If Average Order Value increased, holding
   number of orders constant, what Average Order Value hits the 20% target?"
3. Document the result.

## Deliverable
`day06_solved.xlsx` with a working Power Query (`PQ_Cleaned` sheet) and a
`GoalSeek` sheet showing the what-if result.
