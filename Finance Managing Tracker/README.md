#  Personal Finance Tracker — CLI Edition

A fully-featured, menu-driven command-line finance tracker built in Python. No GUI, no dependencies — just a clean terminal interface to log income, track expenses, view summaries, and manage your money on the go.

---

## 📸 Preview

```
════════════════════════════════════════════════════════════
       💰  PERSONAL FINANCE TRACKER  💰
       📅  23 April 2026  |  09:15 AM
════════════════════════════════════════════════════════════

  ┌──────────────────┬──────────────────┬──────────────────┐
  │   💼 BALANCE     │   📈 INCOME      │   📉 EXPENSES    │
  │   +₨  45,000.00  │   ₨  70,000.00  │   ₨  25,000.00  │
  └──────────────────┴──────────────────┴──────────────────┘
  📋 Total Entries: 8

  MAIN MENU
  ────────────────────────────────────────────────────────
  [1]  ➕  Add Transaction
  [2]  📋  View Transactions
  [3]  🔍  Filter Transactions
  [4]  🗑   Delete a Transaction
  [5]  📊  Category Summary
  [6]  🧹  Clear All Data
  [0]  🚪  Exit
  ────────────────────────────────────────────────────────
  Your choice:
```

### Category Summary View
```
  📊  CATEGORY SUMMARY
  ────────────────────────────────────────────────────────
  Type       Category         Total          Bar
  ────────────────────────────────────────────────────────
  🟢 Income   Salary        +₨  50,000.00  █████████████████████████
  🟢 Income   Freelance     +₨  20,000.00  ██████████
  🔴 Expense  Rent          -₨  15,000.00  ███████
  🔴 Expense  Food          -₨   7,000.00  ███
  🔴 Expense  Transport     -₨   3,000.00  █
```

---

## ✨ Features

- 📊 **Live Summary Banner** — Balance, Total Income & Total Expenses on every screen
- ➕ **Add Transactions** — Log income or expenses with type, category, description, amount & date
- 📋 **View All Transactions** — Clean table with index, date, type, category, description & amount
- 🔍 **Filter Transactions** — View All / Income only / Expense only
- 🗑️ **Delete a Transaction** — Select by number and confirm before deleting
- 📊 **Category Summary** — Visual bar chart of spending/earning per category
- 🧹 **Clear All Data** — Wipe everything with a typed `YES` confirmation
- 💾 **Persistent Storage** — Data saved to `finance_data.json` and restored on every run
- 🟢🔴 **Color Markers** — Instant visual distinction between income and expense rows

---

## 🎮 How to Use

1. **Launch** the app — the summary banner and main menu appear
2. **Press `1`** to add a new transaction:
   - Choose `Income` or `Expense`
   - Pick a category from the list
   - Enter a description and amount
   - Set a date (defaults to today)
3. **Press `2`** to view all transactions in a formatted table
4. **Press `3`** to filter by All / Income / Expense
5. **Press `4`** to delete a transaction by its number
6. **Press `5`** to see a category-by-category breakdown with bar chart
7. **Press `6`** to clear all data (requires typing `YES`)
8. **Press `0`** to exit

---

## 🧩 Code Overview

| Function | Description |
|---|---|
| `load_data()` | Reads `finance_data.json`; returns empty structure if not found |
| `save_data(data)` | Writes updated transactions back to `finance_data.json` |
| `clear()` | Clears the terminal screen (cross-platform) |
| `divider()` | Prints a horizontal separator line |
| `header()` | Clears screen and prints the app title + current date/time |
| `summary_banner(data)` | Displays the Balance / Income / Expense summary cards |
| `main_menu()` | Prints the numbered main menu options |
| `add_transaction(data)` | Guided prompts to add a new income or expense entry |
| `view_transactions(data)` | Renders all (or filtered) transactions as a formatted table |
| `filter_menu(data)` | Prompts for filter type then calls `view_transactions()` |
| `delete_transaction(data)` | Lists entries, prompts for selection, confirms and deletes |
| `category_summary(data)` | Shows a proportional bar chart grouped by type + category |
| `clear_all(data)` | Deletes all transactions after `YES` confirmation |
| `main()` | Main loop — loads data, shows menu, routes to functions |

---

## 📦 Income Categories

| # | Category |
|---|---|
| 1 | Salary |
| 2 | Freelance |
| 3 | Investment |
| 4 | Gift |
| 5 | Other |

## 🛒 Expense Categories

| # | Category |
|---|---|
| 1 | Food |
| 2 | Rent |
| 3 | Transport |
| 4 | Shopping |
| 5 | Utilities |
| 6 | Healthcare |
| 7 | Education |
| 8 | Other |

---

## 💡 Possible Future Improvements

- [ ] Export transactions to **CSV**
- [ ] **Monthly report** — summarize by month automatically
- [ ] **Budget limit** — warn when a category exceeds a set limit
- [ ] **Search** transactions by keyword or date range
- [ ] **Recurring transactions** — auto-add monthly salary etc.
- [ ] **Color output** using `colorama` for richer terminal styling
- [ ] **Password protection** on startup

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Shujaat Hussain**
- GitHub: [@your-username](https://github.com/Shujaa93)

---

> Built with 🖤 and Python — No GUI needed, just results! 
