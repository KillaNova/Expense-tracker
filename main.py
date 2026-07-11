from database import Database
from repository import ExpensesRepository, IncomeRepository
from cli import App

def main():
    db = Database()
    expense_repo = ExpensesRepository(db)
    income_repo = IncomeRepository(db)
    
    app = App(expense_repo, income_repo)
    app.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTot ziens!")