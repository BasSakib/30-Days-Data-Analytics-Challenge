"""
Generates the master sales dataset used across all 30 days of the challenge.
Intentionally includes messy real-world issues (duplicates, missing values,
inconsistent formatting) so Day 04 (Excel data hygiene) and Day 09/22-24
(Power Query / Pandas cleaning) have real problems to solve.

Run: python generate_dataset.py
Output: sales_data_raw.csv (messy, for cleaning exercises)
        sales_data_clean.csv (cleaned, for later-phase exercises)
"""
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

REGIONS = ["North", "South", "East", "West", "Central"]
CATEGORIES = {
    "Electronics": ["Laptop", "Smartphone", "Headphones", "Tablet", "Smartwatch", "Monitor"],
    "Furniture": ["Office Chair", "Desk", "Bookshelf", "Sofa", "Dining Table"],
    "Apparel": ["T-Shirt", "Jeans", "Jacket", "Sneakers", "Cap"],
    "Grocery": ["Rice 5kg", "Cooking Oil 1L", "Tea Pack", "Coffee Jar", "Snack Box"],
    "Stationery": ["Notebook", "Pen Set", "Backpack", "Desk Organizer"],
}
SALES_REPS = [
    "Tanvir Ahmed", "Farzana Islam", "Rakib Hasan", "Nusrat Jahan", "Shakil Rahman",
    "Mim Akter", "Imran Kabir", "Sadia Chowdhury", "Arif Hossain", "Lamia Sultana",
]
CHANNELS = ["Online", "Retail Store", "Distributor", "Wholesale"]
PAYMENT = ["Credit Card", "bKash", "Cash", "Bank Transfer", "Nagad"]

UNIT_PRICES = {
    "Laptop": 850, "Smartphone": 400, "Headphones": 60, "Tablet": 300,
    "Smartwatch": 150, "Monitor": 220, "Office Chair": 120, "Desk": 180,
    "Bookshelf": 90, "Sofa": 450, "Dining Table": 350, "T-Shirt": 15,
    "Jeans": 35, "Jacket": 65, "Sneakers": 55, "Cap": 10, "Rice 5kg": 8,
    "Cooking Oil 1L": 3, "Tea Pack": 4, "Coffee Jar": 7, "Snack Box": 5,
    "Notebook": 2, "Pen Set": 6, "Backpack": 40, "Desk Organizer": 18,
}

start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 12, 31)
date_range_days = (end_date - start_date).days

rows = []
order_id = 10000

for _ in range(3000):
    order_id += 1
    category = random.choice(list(CATEGORIES.keys()))
    product = random.choice(CATEGORIES[category])
    region = random.choice(REGIONS)
    rep = random.choice(SALES_REPS)
    channel = random.choice(CHANNELS)
    payment = random.choice(PAYMENT)
    order_date = start_date + timedelta(days=random.randint(0, date_range_days))
    qty = random.randint(1, 25)
    base_price = UNIT_PRICES[product]
    # small random price variance to simulate discounts/regional pricing
    unit_price = round(base_price * random.uniform(0.9, 1.15), 2)
    revenue = round(qty * unit_price, 2)

    rows.append({
        "OrderID": order_id,
        "OrderDate": order_date.strftime("%Y-%m-%d"),
        "Region": region,
        "SalesRep": rep,
        "Category": category,
        "Product": product,
        "Channel": channel,
        "PaymentMethod": payment,
        "Quantity": qty,
        "UnitPrice": unit_price,
        "Revenue": revenue,
    })

# --- write CLEAN version first ---
clean_path = "/home/claude/30-day-data-journey/data/sales_data_clean.csv"
with open(clean_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

# --- now build a MESSY raw version for Day 01 / Day 04 / Day 09 / Day 22-24 ---
messy_rows = [dict(r) for r in rows]

# 1. Inject ~40 duplicate rows
for _ in range(40):
    messy_rows.append(dict(random.choice(rows)))

# 2. Inject missing values in ~2% of rows (Region, SalesRep, UnitPrice, Quantity)
for r in messy_rows:
    if random.random() < 0.02:
        r["Region"] = ""
    if random.random() < 0.02:
        r["SalesRep"] = ""
    if random.random() < 0.015:
        r["UnitPrice"] = ""
    if random.random() < 0.015:
        r["Quantity"] = ""

# 3. Inconsistent text casing / whitespace for Region and Channel
def messify_text(val):
    choice = random.random()
    if choice < 0.15:
        return val.upper()
    elif choice < 0.30:
        return val.lower()
    elif choice < 0.40:
        return f"  {val}  "
    return val

for r in messy_rows:
    r["Region"] = messify_text(r["Region"]) if r["Region"] else r["Region"]
    r["Channel"] = messify_text(r["Channel"]) if r["Channel"] else r["Channel"]

# 4. Inconsistent date formats (mix of YYYY-MM-DD, DD/MM/YYYY, MM-DD-YYYY)
def messify_date(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    fmt_choice = random.random()
    if fmt_choice < 0.2:
        return dt.strftime("%d/%m/%Y")
    elif fmt_choice < 0.35:
        return dt.strftime("%m-%d-%Y")
    return date_str

for r in messy_rows:
    r["OrderDate"] = messify_date(r["OrderDate"])

# 5. Recompute Revenue is skipped intentionally -- left as-is even where
#    Quantity/UnitPrice are blank, simulating a real messy export.

random.shuffle(messy_rows)

raw_path = "/home/claude/30-day-data-journey/data/sales_data_raw.csv"
with open(raw_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(messy_rows)

print(f"Clean rows: {len(rows)}")
print(f"Raw (messy) rows: {len(messy_rows)}")
print(f"Written to: {clean_path}")
print(f"Written to: {raw_path}")
