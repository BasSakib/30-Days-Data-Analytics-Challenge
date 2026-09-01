# Interview Prep — Day 30

## "Walk me through a project you're proud of."
I built a 30-day self-directed challenge that took one messy sales
dataset all the way through Excel, Power BI, SQL, and Python. The
capstone project ties it together: I loaded the raw ~3,000-row dataset
into SQLite, wrote cleaning queries to fix duplicates and inconsistent
formatting, pulled the cleaned data into Python with pandas to do the
real analysis (top products, regional performance, a profit estimate
feature I engineered), and then built a dashboard on top of the final
output. What I'm proudest of isn't any single step — it's that the same
dataset flows cleanly through every layer, so I can show a reviewer
exactly how a number in the dashboard traces back to a specific row in
the raw file.

## "How do you handle messy or missing data?"
My approach is to diagnose before I fix: I check `.isnull().sum()` (or
`COUNTBLANK` in Excel) to see which columns actually have gaps and how
big they are, rather than guessing. Then I choose a fill strategy that
fits the column — for a categorical field like Region I'll use a
placeholder like "Unknown" so I don't silently drop real orders, but for
a numeric field like UnitPrice, filling with the average for that
specific product is more defensible than a flat global average. I also
always keep a written log of what I changed and why — I did this in a
`CleaningLog` sheet in Excel and as inline comments in my SQL/Python — so
the cleaning decisions are auditable, not just "the data looked fine
after."

## "Tell me about a time you used SQL to answer a business question."
In the SQL phase of this project, I used a window function to answer
"which sales reps are underperforming relative to their own past
performance" — comparing each rep's most recent month's revenue against
their own historical average using `ROW_NUMBER()` and a self-join,
rather than just ranking everyone against each other. That distinction
mattered: a rep with a naturally smaller territory might rank low overall
but still be doing fine relative to their own baseline, while someone
with a strong territory could be quietly declining. The window-function
version answers the more useful business question.

## "What's a DAX measure you've written and what did it do?"
I wrote a month-over-month revenue growth measure using `CALCULATE` with
`DATEADD` to shift the date context back one month, then compared it
against the current month's total with `DIVIDE` (rather than a raw `/`)
so it returns blank instead of an error when there's no prior-month data
to compare against. It's a small detail, but using `DIVIDE()` instead of
`/` is the kind of thing that stops a dashboard from showing a scary
error message the first time someone filters to a period with no
comparison data.

## "How would you explain a dashboard's insight to a non-technical stakeholder?"
I'd lead with the business implication, not the methodology. Instead of
"Electronics has the highest SUM(Revenue) grouped by Category," I'd say
"Electronics is our biggest revenue driver — it's worth protecting that
inventory and double-checking we're not underspending on marketing there
compared to other categories." I keep the chart or number on screen while
I say it, and I only go into how the number was calculated if they ask —
most stakeholders want the "so what," not the formula.
