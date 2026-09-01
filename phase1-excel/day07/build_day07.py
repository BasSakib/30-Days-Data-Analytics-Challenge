import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.chart import BarChart, LineChart, Reference

df = pd.read_csv("/home/claude/30-day-data-journey/data/sales_data_clean.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["MonthLabel"] = df["OrderDate"].dt.strftime("%Y-%m")

wb = Workbook()
ws = wb.active
ws.title = "Sales"

headers = list(df.columns[:-1])  # exclude helper MonthLabel from raw sheet
data_df = df[headers].copy()
data_df["OrderDate"] = data_df["OrderDate"].dt.strftime("%Y-%m-%d")
headers_full = headers + ["MonthLabel"]
ws.append(headers_full)
for row in df.itertuples(index=False):
    r = list(row)
    r[headers.index("OrderDate")] = row.OrderDate.strftime("%Y-%m-%d")
    ws.append(r)
n_rows = ws.max_row

header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
for c in range(1, len(headers_full) + 1):
    cell = ws.cell(row=1, column=c)
    cell.fill = header_fill
    cell.font = Font(name="Arial", bold=True, color="FFFFFF")
for c in range(1, len(headers_full) + 1):
    ws.column_dimensions[get_column_letter(c)].width = 13
ws.freeze_panes = "A2"
tbl = Table(displayName="tbl_Sales", ref=f"A1:{get_column_letter(len(headers_full))}{n_rows}")
tbl.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
ws.add_table(tbl)

region_col = get_column_letter(headers_full.index("Region") + 1)
revenue_col = get_column_letter(headers_full.index("Revenue") + 1)
qty_col = get_column_letter(headers_full.index("Quantity") + 1)
product_col = get_column_letter(headers_full.index("Product") + 1)
month_col = get_column_letter(headers_full.index("MonthLabel") + 1)

# --- Dashboard sheet ---
dash = wb.create_sheet("Dashboard", 0)
dash.sheet_view.showGridLines = False
dash["B2"] = "SALES PERFORMANCE DASHBOARD"
dash["B2"].font = Font(name="Arial", bold=True, size=18, color="1F4E78")

# KPI cards
kpi_fill = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
kpis = [
    ("Total Revenue", f"=SUM(Sales!{revenue_col}:{revenue_col})", '"$"#,##0'),
    ("Total Orders", f"=COUNTA(Sales!A2:A{n_rows})", "#,##0"),
    ("Average Order Value", f"=SUM(Sales!{revenue_col}:{revenue_col})/COUNTA(Sales!A2:A{n_rows})", '"$"#,##0.00'),
    ("Total Quantity Sold", f"=SUM(Sales!{qty_col}:{qty_col})", "#,##0"),
]
col_start = 2
for i, (label, formula, numfmt) in enumerate(kpis):
    col = col_start + i * 3
    label_cell = dash.cell(row=4, column=col, value=label)
    label_cell.font = Font(name="Arial", bold=True, size=10, color="1F4E78")
    val_cell = dash.cell(row=5, column=col, value=formula)
    val_cell.font = Font(name="Arial", bold=True, size=16)
    val_cell.number_format = numfmt
    for rr in (4, 5):
        for cc in (col, col + 1):
            dash.cell(row=rr, column=cc).fill = kpi_fill
    dash.merge_cells(start_row=4, start_column=col, end_row=4, end_column=col + 1)
    dash.merge_cells(start_row=5, start_column=col, end_row=5, end_column=col + 1)

# Helper region summary table (source for bar chart)
regions = sorted(df["Region"].unique())
r0 = 8
dash.cell(row=r0, column=1, value="Region").font = Font(bold=True)
dash.cell(row=r0, column=2, value="Revenue").font = Font(bold=True)
for i, reg in enumerate(regions, start=1):
    dash.cell(row=r0 + i, column=1, value=reg)
    dash.cell(row=r0 + i, column=2,
              value=f'=SUMIFS(Sales!{revenue_col}:{revenue_col},Sales!{region_col}:{region_col},A{r0+i})'
              ).number_format = '"$"#,##0'
region_end = r0 + len(regions)

# Helper monthly summary table (source for line chart)
months = sorted(df["MonthLabel"].unique())
m0 = region_end + 3
dash.cell(row=m0, column=1, value="Month").font = Font(bold=True)
dash.cell(row=m0, column=2, value="Revenue").font = Font(bold=True)
for i, m in enumerate(months, start=1):
    dash.cell(row=m0 + i, column=1, value=m)
    dash.cell(row=m0 + i, column=2,
              value=f'=SUMIFS(Sales!{revenue_col}:{revenue_col},Sales!{month_col}:{month_col},A{m0+i})'
              ).number_format = '"$"#,##0'
month_end = m0 + len(months)

# Top 5 products table
top5 = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)
t0 = month_end + 3
dash.cell(row=t0, column=1, value="Top 5 Products by Revenue").font = Font(bold=True, size=12)
dash.cell(row=t0 + 1, column=1, value="Product").font = Font(bold=True)
dash.cell(row=t0 + 1, column=2, value="Revenue").font = Font(bold=True)
for i, prod in enumerate(top5.index, start=1):
    dash.cell(row=t0 + 1 + i, column=1, value=prod)
    dash.cell(row=t0 + 1 + i, column=2,
              value=f'=SUMIFS(Sales!{revenue_col}:{revenue_col},Sales!{product_col}:{product_col},A{t0+1+i})'
              ).number_format = '"$"#,##0'

# Bar chart: Revenue by Region
bar = BarChart()
bar.title = "Revenue by Region"
bar.y_axis.title = "Revenue ($)"
data_ref = Reference(dash, min_col=2, min_row=r0, max_row=region_end)
cats_ref = Reference(dash, min_col=1, min_row=r0 + 1, max_row=region_end)
bar.add_data(data_ref, titles_from_data=True)
bar.set_categories(cats_ref)
bar.height, bar.width = 8, 15
dash.add_chart(bar, "E8")

# Line chart: monthly revenue trend
line = LineChart()
line.title = "Revenue Trend by Month"
line.y_axis.title = "Revenue ($)"
data_ref2 = Reference(dash, min_col=2, min_row=m0, max_row=month_end)
cats_ref2 = Reference(dash, min_col=1, min_row=m0 + 1, max_row=month_end)
line.add_data(data_ref2, titles_from_data=True)
line.set_categories(cats_ref2)
line.height, line.width = 8, 15
dash.add_chart(line, "E24")

# Slicer note (attach in real Excel via a PivotTable if interactivity is needed)
note_cell = dash.cell(row=t0 + 8, column=1,
    value=("Note: this dashboard uses live SUMIFS formulas driven by tbl_Sales. "
           "For a clickable Region/Channel slicer, insert a PivotTable from tbl_Sales "
           "and add Insert > Slicer — connect it to a PivotChart alongside these charts."))
note_cell.font = Font(italic=True, size=9)
note_cell.alignment = Alignment(wrap_text=True)
dash.merge_cells(start_row=t0 + 8, start_column=1, end_row=t0 + 8, end_column=6)

for col, width in [("A", 20), ("B", 14), ("C", 14), ("D", 4), ("E", 12)]:
    dash.column_dimensions[col].width = width

wb.move_sheet("Dashboard", offset=-len(wb.sheetnames))
wb.save("/home/claude/30-day-data-journey/phase1-excel/day07/day07_solved.xlsx")
print("Day 07 saved (pre-recalc).")
