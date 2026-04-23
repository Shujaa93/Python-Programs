import json
import os
from datetime import datetime

# ─── Data File ───────────────────────────────────────────────────────────────
DATA_FILE = "finance_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"transactions": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ─── Display Helpers ─────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def divider(char="─", width=60):
    print(char * width)

def header():
    clear()
    divider("═")
    print("       💰  PERSONAL FINANCE TRACKER  💰")
    print(f"       📅  {datetime.now().strftime('%d %B %Y  |  %I:%M %p')}")
    divider("═")

def summary_banner(data):
    transactions = data["transactions"]
    total_in  = sum(t["amount"] for t in transactions if t["type"] == "Income")
    total_out = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    balance   = total_in - total_out
    count     = len(transactions)

    bal_sign = "+" if balance >= 0 else ""

    print(f"""
  ┌──────────────────┬──────────────────┬──────────────────┐
  │   💼 BALANCE     │   📈 INCOME      │   📉 EXPENSES    │
  │  {bal_sign}₨ {balance:>10.2f}  │   ₨ {total_in:>10.2f}  │   ₨ {total_out:>10.2f}  │
  └──────────────────┴──────────────────┴──────────────────┘
  📋 Total Entries: {count}
""")

# ─── Menu ────────────────────────────────────────────────────────────────────
def main_menu():
    print("  MAIN MENU")
    divider()
    print("  [1]  ➕  Add Transaction")
    print("  [2]  📋  View Transactions")
    print("  [3]  🔍  Filter Transactions")
    print("  [4]  🗑   Delete a Transaction")
    print("  [5]  📊  Category Summary")
    print("  [6]  🧹  Clear All Data")
    print("  [0]  🚪  Exit")
    divider()

# ─── Add Transaction ─────────────────────────────────────────────────────────
CATEGORIES = {
    "Income":  ["Salary", "Freelance", "Investment", "Gift", "Other"],
    "Expense": ["Food", "Rent", "Transport", "Shopping",
                "Utilities", "Healthcare", "Education", "Other"],
}

def add_transaction(data):
    header()
    print("  ➕  ADD NEW TRANSACTION")
    divider()

    # Type
    print("\n  Type:")
    print("  [1] Income")
    print("  [2] Expense")
    while True:
        choice = input("\n  Select (1/2): ").strip()
        if choice == "1":
            ttype = "Income"
            break
        elif choice == "2":
            ttype = "Expense"
            break
        print("  ⚠  Invalid choice. Enter 1 or 2.")

    # Category
    cats = CATEGORIES[ttype]
    print(f"\n  Category:")
    for i, c in enumerate(cats, 1):
        print(f"  [{i}] {c}")
    while True:
        try:
            ci = int(input(f"\n  Select (1-{len(cats)}): "))
            if 1 <= ci <= len(cats):
                category = cats[ci - 1]
                break
        except ValueError:
            pass
        print(f"  ⚠  Enter a number between 1 and {len(cats)}.")

    # Description
    while True:
        desc = input("\n  Description: ").strip()
        if desc:
            break
        print("  ⚠  Description cannot be empty.")

    # Amount
    while True:
        try:
            amount = float(input("  Amount (₨): ").strip())
            if amount > 0:
                break
            print("  ⚠  Amount must be greater than 0.")
        except ValueError:
            print("  ⚠  Enter a valid number.")

    # Date
    default_date = datetime.now().strftime("%Y-%m-%d")
    while True:
        date_input = input(f"  Date (YYYY-MM-DD) [{default_date}]: ").strip()
        if date_input == "":
            date_input = default_date
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("  ⚠  Invalid date format. Use YYYY-MM-DD.")

    data["transactions"].append({
        "date": date_input,
        "type": ttype,
        "category": category,
        "description": desc,
        "amount": amount,
    })
    save_data(data)

    sign = "+" if ttype == "Income" else "-"
    print(f"\n  ✅  Transaction saved!  {sign}₨{amount:,.2f}  [{category}]")
    input("\n  Press Enter to continue...")

# ─── View Transactions ───────────────────────────────────────────────────────
def view_transactions(data, filter_type="All"):
    header()
    title = f"📋  TRANSACTIONS" + (f"  ({filter_type} only)" if filter_type != "All" else "")
    print(f"  {title}")
    divider()

    transactions = [
        (i, t) for i, t in enumerate(data["transactions"])
        if filter_type == "All" or t["type"] == filter_type
    ]

    if not transactions:
        print("\n  No transactions found.\n")
        input("  Press Enter to continue...")
        return

    # Table header
    print(f"\n  {'#':<4} {'Date':<12} {'Type':<8} {'Category':<14} {'Description':<22} {'Amount':>12}")
    divider()

    for idx, (orig_i, t) in enumerate(transactions, 1):
        sign   = "+" if t["type"] == "Income" else "-"
        amt    = f"{sign}₨{t['amount']:,.2f}"
        desc   = t["description"][:20] + ".." if len(t["description"]) > 20 else t["description"]
        marker = "🟢" if t["type"] == "Income" else "🔴"
        print(f"  {idx:<4} {t['date']:<12} {marker} {t['type']:<6} {t['category']:<14} {desc:<22} {amt:>12}")

    divider()
    print(f"  Showing {len(transactions)} record(s)\n")
    input("  Press Enter to continue...")

# ─── Filter Transactions ─────────────────────────────────────────────────────
def filter_menu(data):
    header()
    print("  🔍  FILTER TRANSACTIONS")
    divider()
    print("  [1]  All Transactions")
    print("  [2]  Income Only")
    print("  [3]  Expense Only")
    divider()
    choice = input("  Select (1/2/3): ").strip()
    mapping = {"1": "All", "2": "Income", "3": "Expense"}
    view_transactions(data, mapping.get(choice, "All"))

# ─── Delete Transaction ──────────────────────────────────────────────────────
def delete_transaction(data):
    header()
    print("  🗑   DELETE A TRANSACTION")
    divider()

    if not data["transactions"]:
        print("\n  No transactions to delete.\n")
        input("  Press Enter to continue...")
        return

    for i, t in enumerate(data["transactions"], 1):
        sign = "+" if t["type"] == "Income" else "-"
        print(f"  [{i}]  {t['date']}  {t['type']:<8}  {t['category']:<14}  "
              f"{t['description']:<22}  {sign}₨{t['amount']:,.2f}")

    divider()
    try:
        idx = int(input("  Enter # to delete (0 to cancel): ").strip())
        if idx == 0:
            return
        if 1 <= idx <= len(data["transactions"]):
            t = data["transactions"][idx - 1]
            confirm = input(f"\n  Delete '{t['description']}' ₨{t['amount']:,.2f}? (y/n): ").lower()
            if confirm == "y":
                data["transactions"].pop(idx - 1)
                save_data(data)
                print("  ✅  Transaction deleted.")
            else:
                print("  ❌  Cancelled.")
        else:
            print("  ⚠  Invalid number.")
    except ValueError:
        print("  ⚠  Invalid input.")

    input("\n  Press Enter to continue...")

# ─── Category Summary ────────────────────────────────────────────────────────
def category_summary(data):
    header()
    print("  📊  CATEGORY SUMMARY")
    divider()

    if not data["transactions"]:
        print("\n  No data available.\n")
        input("  Press Enter to continue...")
        return

    summary = {}
    for t in data["transactions"]:
        key = (t["type"], t["category"])
        summary[key] = summary.get(key, 0) + t["amount"]

    print(f"\n  {'Type':<10} {'Category':<16} {'Total':>14}  {'Bar'}")
    divider()

    max_amt = max(summary.values()) if summary else 1
    for (ttype, cat), total in sorted(summary.items(), key=lambda x: -x[1]):
        bar_len = int((total / max_amt) * 25)
        bar     = "█" * bar_len
        sign    = "+" if ttype == "Income" else "-"
        marker  = "🟢" if ttype == "Income" else "🔴"
        print(f"  {marker} {ttype:<8} {cat:<16} {sign}₨{total:>10,.2f}  {bar}")

    divider()
    input("\n  Press Enter to continue...")

# ─── Clear All ───────────────────────────────────────────────────────────────
def clear_all(data):
    header()
    print("  🧹  CLEAR ALL DATA")
    divider()

    if not data["transactions"]:
        print("\n  Nothing to clear.\n")
        input("  Press Enter to continue...")
        return

    print(f"\n  ⚠  This will delete ALL {len(data['transactions'])} transactions.")
    confirm = input("  Are you sure? Type YES to confirm: ").strip()
    if confirm == "YES":
        data["transactions"] = []
        save_data(data)
        print("\n    All data cleared.")
    else:
        print("\n    Cancelled.")

    input("\n  Press Enter to continue...")

# ─── Main Loop ───────────────────────────────────────────────────────────────
def main():
    data = load_data()

    while True:
        header()
        summary_banner(data)
        main_menu()

        choice = input("  Your choice: ").strip()

        if choice == "1":
            add_transaction(data)
        elif choice == "2":
            view_transactions(data)
        elif choice == "3":
            filter_menu(data)
        elif choice == "4":
            delete_transaction(data)
        elif choice == "5":
            category_summary(data)
        elif choice == "6":
            clear_all(data)
        elif choice == "0":
            header()
            print("\n  👋  Thanks for using Finance Tracker. Goodbye!\n")
            divider()
            break
        else:
            print("  ⚠  Invalid choice. Please try again.")
            input("  Press Enter to continue...")

if __name__ == "__main__":
    main()
