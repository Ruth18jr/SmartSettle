# SmartSettle

SmartSettle is a Python command-line app that helps groups split shared restaurant bills and figure out who should pay whom.

## What Problem Does It Solve?

Splitting a bill can get confusing when different people pay different amounts, order different items, or owe different totals. SmartSettle keeps track of each person's owed amount and paid amount, then creates a simple settlement plan so the group can balance everything out.

SmartSettle supports:

- Equal bill splitting
- Usage-based splitting
- Balance tracking
- Optimized settlement suggestions
- Saved transaction history

## Technologies Used

- Python
- JSON for saving transaction history
- A command-line menu for user input

The project is organized into separate modules:

- `main.py` runs the menu and collects user input.
- `equal_split.py` calculates equal splits.
- `usage_split.py` calculates usage-based splits.
- `ledger.py` stores and displays balances.
- `optimizer.py` creates the settlement plan.
- `history.py` saves and displays past transactions.
- `transactions.json` stores saved transaction history.

## How To Run It

1. Make sure Python is installed on your computer.
2. Open a terminal.
3. Go into the SmartSettle folder:

```bash
cd SmartSettle
```

4. Run the app:

```bash
python3 main.py
```

5. Choose an option from the menu:

```text
1. Equal split
2. Usage-based split
3. Show history
4. Exit
```

## Example Use

If one person paid more than their share and another person paid less, SmartSettle will show each person's balance and print a settlement plan, such as:

```text
Alex pays Jordan $12.50
```

This helps the group settle up without manually calculating every payment.
