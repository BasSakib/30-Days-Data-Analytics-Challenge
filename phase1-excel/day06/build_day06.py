import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

raw = pd.read_csv("/home/claude/30-day-data-journey/data/sales_data_raw.csv")

# Replicate the Power Query steps in Python (same logic, documented as "Applied Steps")
df = raw.drop_duplicates(subset=["OrderID"]).copy()
df["Region"] = df["Region"].astype(str).str.strip().str.title().replace({"Nan": "Unknown", "": "Unknown"})
df["Channel"] = df["Channel"].astype(str).str.strip().str.title()
df["SalesRep"] = df["SalesRep"].fillna("Unknown").astype(str).str.strip().replace("", "Unknown")

# Parse mixed date formats
def parse_mixed_date(s):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return pd.to_datetime(s, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT

df["OrderDate"] = df["OrderDate"].apply(parse_mixed_date)

avg_price_by_product = df.groupby("Product")["UnitPrice"].transform("mean")
df["UnitPrice"] = df["UnitPrice"].fillna(avg_price_by_product).round(2)
df["Quantity"] = df["Quantity"].fillna(1)

wb = Workbook()
ws = wb.active
ws.title = "PQ_Cleaned"

headers = list(df.columns)
ws.append(headers)
for row in df.itertuples(index=False):
    vals = list(row)
    ws.append(vals)
n_rows = ws.max_row

date_col = headers.index("OrderDate") + 1
for r in range(2, n_rows + 1):
    ws.cell(row=r, column=date_col).number_format = "YYYY-MM-DD"

header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
for c in range(1, len(headers) + 1):
    cell = ws.cell(row=1, column=c)
    cell.fill = header_fill
    cell.font = Font(name="Arial", bold=True, color="FFFFFF")
for c in range(1, len(headers) + 1):
    ws.column_dimensions[get_column_letter(c)].width = 14
ws.freeze_panes = "A2"
tbl = Table(displayName="tbl_PQCleaned", ref=f"A1:{get_column_letter(len(headers))}{n_rows}")
tbl.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
ws.add_table(tbl)

# --- Applied Steps documentation (mirrors the Power Query editor's step list) ---
notes = wb.create_sheet("PQ_Applied_Steps")
notes["A1"] = "Power Query — Applied Steps"
notes["A1"].font = Font(name="Arial", bold=True, size=14)
steps = [
    "1. Source: Imported sales_data_raw.csv",
    "2. Removed Duplicates: based on OrderID column",
    "3. Trimmed & Cleaned Text: Region, Channel, SalesRep",
    "4. Capitalized Each Word: Region, Channel",
    "5. Custom Column: parsed OrderDate across 3 detected formats "
    "(YYYY-MM-DD, DD/MM/YYYY, MM-DD-YYYY) into a single Date type",
    "6. Replaced Values: blank Region/SalesRep -> 'Unknown'",
    "7. Filled Down/Replaced: blank UnitPrice -> average UnitPrice per Product",
    "8. Replaced Values: blank Quantity -> 1",
    "9. Changed Type: OrderDate -> Date, UnitPrice/Revenue -> Decimal, Quantity -> Whole Number",
    "10. Loaded to: PQ_Cleaned sheet",
    "",
    "Refreshing this query (Data > Refresh All in a real Power Query workbook) re-runs",
    "every step above in order against the latest source file — that repeatability is",
    "the entire point of doing cleaning in Power Query instead of manually.",
]
for i, line in enumerate(steps, start=3):
    notes.cell(row=i, column=1, value=line).font = Font(name="Arial", size=11)
notes.column_dimensions["A"].width = 95

# --- Goal Seek sheet ---
gs = wb.create_sheet("GoalSeek")
gs["A1"] = "Goal Seek — Revenue Target Analysis"
gs["A1"].font = Font(name="Arial", bold=True, size=14)

total_revenue = df["Revenue"].sum()
total_orders = len(df)
current_aov = total_revenue / total_orders
target_revenue = total_revenue * 1.20
target_aov = target_revenue / total_orders

rows = [
    ("Current Total Revenue", "=Total_Orders*Current_AOV", total_revenue, '"$"#,##0.00'),
    ("Total Orders (constant)", None, total_orders, "#,##0"),
    ("Current Average Order Value", None, round(current_aov, 2), '"$"#,##0.00'),
    ("Target Total Revenue (+20%)", "=B3*1.2", target_revenue, '"$"#,##0.00'),
    ("Required Average Order Value", "=B6/B4", round(target_aov, 2), '"$"#,##0.00'),
]
gs["A3"] = "Current Total Revenue"
gs["B3"] = round(total_revenue, 2)
gs["B3"].number_format = '"$"#,##0.00'
gs["A4"] = "Total Orders (held constant)"
gs["B4"] = total_orders
gs["A5"] = "Current Average Order Value"
gs["B5"] = "=B3/B4"
gs["B5"].number_format = '"$"#,##0.00'
gs["A6"] = "Target Total Revenue (+20%)"
gs["B6"] = "=B3*1.2"
gs["B6"].number_format = '"$"#,##0.00'
gs["A7"] = "Goal Seek Result: Required Average Order Value"
gs["B7"] = "=B6/B4"
gs["B7"].number_format = '"$"#,##0.00'
gs["A7"].font = Font(bold=True)
gs["B7"].font = Font(bold=True)

for r in range(3, 8):
    gs.cell(row=r, column=1).font = Font(name="Arial")
gs.column_dimensions["A"].width = 40
gs.column_dimensions["B"].width = 16

note = gs.cell(row=9, column=1,
    value=("In Excel: Data > What-If Analysis > Goal Seek — Set cell B3, To value = target, "
           "By changing cell B5. This sheet shows the equivalent result computed with formulas "
           "since Goal Seek itself is an interactive Excel feature, not a storable formula."))
note.font = Font(italic=True, size=9, name="Arial")
note.alignment = Alignment(wrap_text=True)
gs.row_dimensions[9].height = 30

wb.save("/home/claude/30-day-data-journey/phase1-excel/day06/day06_solved.xlsx")
print("Day 06 saved (pre-recalc).")
