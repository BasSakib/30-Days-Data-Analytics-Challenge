import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.chart import BarChart, Reference

df = pd.read_csv("/home/claude/30-day-data-journey/data/sales_data_clean.csv")

wb = Workbook()
ws = wb.active
ws.title = "Sales"

headers = list(df.columns)
ws.append(headers)
for row in df.itertuples(index=False):
    ws.append(list(row))
n_rows = ws.max_row

header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
for c in range(1, len(headers) + 1):
    cell = ws.cell(row=1, column=c)
    cell.fill = header_fill
    cell.font = Font(name="Arial", bold=True, color="FFFFFF")
for c in range(1, len(headers) + 1):
    ws.column_dimensions[get_column_letter(c)].width = 14
ws.freeze_panes = "A2"
tbl = Table(displayName="tbl_Sales", ref=f"A1:{get_column_letter(len(headers))}{n_rows}")
tbl.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
ws.add_table(tbl)

region_col, category_col, revenue_col, channel_col, rep_col = "C", "E", "K", "G", "D"

# --- PivotAnalysis sheet (SUMIFS-driven, functions as a live pivot summary) ---
pv = wb.create_sheet("PivotAnalysis")
pv["A1"] = "Pivot-Style Analysis — Day 05"
pv["A1"].font = Font(name="Arial", bold=True, size=14)
pv["A2"] = ("Built with SUMIFS formulas (equivalent output to a manually-inserted "
            "Excel PivotTable — insert a real PivotTable via Insert > PivotTable "
            "using this same tbl_Sales range for the interactive version).")
pv["A2"].font = Font(name="Arial", italic=True, size=9)
pv.column_dimensions["A"].width = 60

regions = sorted(df["Region"].unique())
categories = sorted(df["Category"].unique())

# 1. Revenue by Region
r = 4
pv.cell(row=r, column=1, value="Revenue by Region").font = Font(bold=True, name="Arial")
r += 1
pv.cell(row=r, column=1, value="Region").font = Font(bold=True)
pv.cell(row=r, column=2, value="Total Revenue").font = Font(bold=True)
region_start_row = r + 1
r += 1
for reg in regions:
    pv.cell(row=r, column=1, value=reg)
    pv.cell(row=r, column=2,
            value=f'=SUMIFS(Sales!{revenue_col}:{revenue_col},Sales!{region_col}:{region_col},A{r})'
            ).number_format = '"$"#,##0.00'
    r += 1
region_end_row = r - 1

# 2. Revenue by Category
r += 1
pv.cell(row=r, column=1, value="Revenue by Category").font = Font(bold=True, name="Arial")
r += 1
pv.cell(row=r, column=1, value="Category").font = Font(bold=True)
pv.cell(row=r, column=2, value="Total Revenue").font = Font(bold=True)
r += 1
for cat in categories:
    pv.cell(row=r, column=1, value=cat)
    pv.cell(row=r, column=2,
            value=f'=SUMIFS(Sales!{revenue_col}:{revenue_col},Sales!{category_col}:{category_col},A{r})'
            ).number_format = '"$"#,##0.00'
    r += 1

# 3. Revenue by Region + Category matrix
r += 1
pv.cell(row=r, column=1, value="Revenue by Region x Category").font = Font(bold=True, name="Arial")
r += 1
matrix_header_row = r
pv.cell(row=r, column=1, value="Region")
for j, cat in enumerate(categories, start=2):
    pv.cell(row=r, column=j, value=cat).font = Font(bold=True)
r += 1
for reg in regions:
    pv.cell(row=r, column=1, value=reg).font = Font(bold=True)
    for j, cat in enumerate(categories, start=2):
        col_letter = get_column_letter(j)
        pv.cell(row=r, column=j,
                value=(f'=SUMIFS(Sales!{revenue_col}:{revenue_col},'
                       f'Sales!{region_col}:{region_col},$A{r},'
                       f'Sales!{category_col}:{category_col},{col_letter}${matrix_header_row})')
                ).number_format = '"$"#,##0.00'
    r += 1

# 4. Top 5 SalesReps by Revenue
r += 1
pv.cell(row=r, column=1, value="Top 5 SalesReps by Revenue").font = Font(bold=True, name="Arial")
r += 1
pv.cell(row=r, column=1, value="SalesRep").font = Font(bold=True)
pv.cell(row=r, column=2, value="Total Revenue").font = Font(bold=True)
r += 1
rep_totals = df.groupby("SalesRep")["Revenue"].sum().sort_values(ascending=False).head(5)
top5_start = r
for rep in rep_totals.index:
    pv.cell(row=r, column=1, value=rep)
    pv.cell(row=r, column=2,
            value=f'=SUMIFS(Sales!{revenue_col}:{revenue_col},Sales!{rep_col}:{rep_col},A{r})'
            ).number_format = '"$"#,##0.00'
    r += 1
top5_end = r - 1

# --- Pivot chart: bar chart of Revenue by Region ---
chart = BarChart()
chart.title = "Revenue by Region"
chart.x_axis.title = "Region"
chart.y_axis.title = "Revenue ($)"
data_ref = Reference(pv, min_col=2, min_row=region_start_row - 1, max_row=region_end_row)
cats_ref = Reference(pv, min_col=1, min_row=region_start_row, max_row=region_end_row)
chart.add_data(data_ref, titles_from_data=True)
chart.set_categories(cats_ref)
chart.height = 8
chart.width = 16
pv.add_chart(chart, f"E4")

# --- Slicer note (native slicers require a real PivotTable object; documented here) ---
note_row = r + 2
pv.cell(row=note_row, column=1,
        value=("Note: Native Excel Slicers attach only to real PivotTable/PivotChart "
               "objects. In Excel, select any cell in tbl_Sales, Insert > PivotTable, "
               "then Insert > Slicer (choose Channel) to add an interactive slicer "
               "connected to these views.")
        ).font = Font(italic=True, size=9, name="Arial")

wb.save("/home/claude/30-day-data-journey/phase1-excel/day05/day05_solved.xlsx")
print("Day 05 saved (pre-recalc).")
