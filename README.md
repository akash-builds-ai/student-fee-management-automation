# Student Fee Management Project

A beginner-friendly business automation project combining Google Sheets and Python to organize student fee records, validate data, and generate reports.

## 1. Spreadsheet Automation

**Tool:** Google Sheets

### Features
- Counts total student records.
- Summarizes Pending and Clear students.
- Calculates total known Fee Due.
- Flags records with missing fee information.
- Highlights repeated student names for review.
- Uses formulas, conditional formatting, and data validation.
- Cleans text using TRIM and PROPER.

## 2. Python Automation

**Tools:** Python, CSV, dictionaries, lists, functions, exception handling

### Features
- Reads student records from `students.csv`.
- Calculates student counts and total known Fee Due.
- Detects missing, invalid, and negative fee values.
- Validates student status values (`Pending` and `Clear`).
- Identifies duplicate names without deleting records.
- Generates `fee_report.txt` automatically.

## Project Files

- `student_fee_automation.py` — Main Python script.
- `students.csv` — Fictional sample student records.
- `fee_report.txt` — Generated summary and validation report.
- `Screenshots/` — Project screenshots.

## How to Run the Python Script

1. Install Python 3.
2. Open a terminal in this project folder.
3. Run:

   ```bash
   python student_fee_automation.py
   ```

The script reads `students.csv` and generates `fee_report.txt`.

## Sample Results

- Total students: 8
- Pending students: 6
- Clear students: 2
- Total known Fee Due: ₹17,500
- Records to review: 1

One sample record has a missing Fee Due value. The script flags it for review instead of assuming the missing amount is zero. The sample data also contains two different student records with the name Aarav; both are retained.

## Learning Outcomes

This project demonstrates practical spreadsheet skills, Python programming, CSV processing, data validation, and automated reporting.

## Data Disclaimer

All included student records are fictional and intended for educational and portfolio demonstration purposes.