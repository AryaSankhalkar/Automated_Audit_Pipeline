Automated Audit Pipeline
This project is a tool I built to help find mistakes in retail sales data. Instead of checking thousands of rows by hand, I used Oracle SQL to organize the data and Python to scan it for errors automatically.

How it works:
The data lives in a table I created in an Oracle database. I then move that data into Python using a CSV file. Once the data is in Python, the script runs through every row and checks for three specific problems:
1.Negative Quantities: It flags any sale where the number of items is 0 or less, which usually means there was a typo during data entry.
2.Date Errors: It looks for "future dates" sales that are dated in the future, which shouldn't be possible.
3.Price Checks: It monitors specific high-value items (like Product 101) to make sure they weren't accidentally sold for too low a price.

Why I built it this way
I chose to use SQL for the storage because it’s the standard for professional databases, and Python (Pandas) for the logic because it’s much faster at handling complex checks than doing it inside a spreadsheet. This setup is a small-scale version of the "ETL" pipelines used by data engineers to keep company records clean and accurate.

Files in this repo
audit_system.py: The Python engine that does the actual auditing.
audit_pipeline.sql: The database code used to create the sales table.