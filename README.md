# expense-tracker-python
A simple command-line **Expense Tracker** built in Python to help you record, view, and summarize your daily expenses.

## Features

- Add new expenses with:
  - Date
  - Category (e.g., Food, Travel, Clothes, Electronic_Devices, Self_care, etc.)
  - Description
  - Amount
- View all recorded transactions
- Calculate total expense
- Simple menu-driven interface

## How to Run

1. Make sure you have Python installed (Python 3.x recommended).
2. Clone or download this repository.
3. Open your terminal/command prompt in the project folder.
4. Run the script:

```bash
python expense_tracker.py
```

5. Follow the menu options:
   - '1' – Add Expense  
   - '2' – View Expenses  
   - '3' – Total Expense  
   - '4' – Exit

## Usage Example

```text
WELCOME TO EXPENSE TRACKER
------Menu------
1. Add Expense
2. View Expense
3. Total Expense
4. Exit
Enter Your Choice:-1
Enter the Date of Transaction:-2026-05-28
Enter The Category(Food,Travel,Clothes,Electronic_Devices,Self_care,etc):-Food
Enter More Detail Description About Category:-Lunch at restaurant
Enter Your Amount:-250

Expenses Added Successfully
```

## Project Structure

```text
expense-tracker/
├── expense_tracker.py   # Main script
└── README.md            # This file
```

## Future Enhancements 

- Save expenses to a file (CSV/JSON) so data persists after closing the program
- Add filtering by category or date
- Add monthly/weekly expense summaries
- Simple charts for expense distribution

## License

This project is open-source and available for personal and educational use
