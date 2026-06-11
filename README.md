# SmartSettle

SmartSettle is a Python-based command-line application that helps groups fairly split shared expenses and calculate the simplest way to settle outstanding balances.

## Overview

Managing shared expenses can become complicated when individuals contribute different amounts or consume different portions of a bill. SmartSettle automates the process by tracking what each participant owes, what they paid, and generating an optimized settlement plan to balance all accounts.

## Features

- Equal bill splitting
- Usage-based expense splitting
- Individual balance tracking
- Optimized settlement calculations
- Transaction history storage and retrieval
- Simple command-line interface

## Technologies Used

- Python
- JSON for data persistence
- Modular software design

## Project Structure

- `main.py` - User interface and application flow
- `equal_split.py` - Equal expense distribution logic
- `usage_split.py` - Usage-based expense calculations
- `ledger.py` - Balance management and tracking
- `optimizer.py` - Settlement optimization algorithm
- `history.py` - Transaction history management
- `transactions.json` - Persistent transaction storage

## How To Run

1. Ensure Python 3 is installed.
2. Open a terminal.
3. Navigate to the project directory:

```bash
cd SmartSettle
```

4. Run the application:

```bash
python3 main.py
```

5. Select an option from the menu:

- Equal Split
- Usage-Based Split
- Show Transaction History
- Exit

## Example

Suppose a group shares a restaurant bill and one person pays more than their share while another pays less. SmartSettle calculates the balances and generates a settlement plan such as:

```text
Alex pays Jordan $12.50
```

This minimizes manual calculations and provides a clear path for settling group expenses.

## Future Improvements

- Graphical User Interface (GUI)
- Receipt scanning and bill import
- AI-powered expense insights
- Cloud-based data storage
- Mobile application support

## Author

Ruth Yared Zewdie

Computer Science student focused on software development, problem-solving, and AI-powered applications.
