import csv
from models import Expense

class CsvImporter:
    def __init__(self, expense_repo):
        self.expense_repo = expense_repo

    def import_expenses(self, filename):
        imported = 0
        skipped = 0

        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    expense = Expense(
                        float(row["amount"]),
                        row["category"],
                        row["description"],
                        row["date"]
                    )
                    self.expense_repo.add(expense)
                    imported += 1
                except (ValueError, KeyError):
                    skipped += 1
        
        print(f"Import klaar: {imported} toegevoegd, {skipped} overgeslagen.")
            