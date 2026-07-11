from datetime import date
from models import Expense, Income

class App:
    def __init__(self, expense_repo, income_repo):
        self.expense_repo = expense_repo
        self.income_repo = income_repo

    def show_menu(self):
        print("\n==== EXPENSE TRACKER - ZZP ADMIN ====")
        print("1. Uitgaven toevoegen")
        print("2. Uitgaven tonen")
        print("3. Uitgaven verwijderen")
        print("4. Inkomst toevoegen")
        print("5. Inkomsten tonen")
        print("0. Afsluiten")
        print("=======================================")

    def add_expense(self):
        amount = float(input("Bedrag €"))
        category = input("Categorie: ")
        description = input("Omschrijving: ")
        expense = Expense(amount, category, description, date.today().isoformat())
        self.expense_repo.add(expense)
        print("Uitgave toegevoegd.")

    def show_expenses(self):
        rows = self.expense_repo.get_all()
        if not rows:
            print("Geen uitgaven.")
            return
        for id, amount, category, description, d in rows:
            print(f"[{id}] €{amount:.2f} | {category} | {description} | {d}")
    
    def add_income(self):
        amount = float(input("Bedrag: €"))
        source = input("Van wie/wat? ")
        description = input("Omschrijving: ")
        income = Income(amount, source, description, date.today().isoformat())
        self.income_repo.add(income)
        print("Inkomst toegevoegd.")

    def show_income(self):
        rows = self.income_repo.get_all()
        if not rows:
            print("Geen inkomsten.")
            return
        for id, amount, source, description, d in rows:
            print(f"[{id}] €{amount:.2f} | {source} | {description} | {d}")


    def delete_expense(self):
        self.show_expense()
        count = self.expense_repo.delete(int(input("Welk id verwijderen")))
        print("Verwijderd." if count else "Niet gevonden.")
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Keuze: ")
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.show_expenses()
            elif choice == "3":
                self.delete_expense()
            elif choice == "4":
                self.add_income()
            elif choice == "5":
                self.show_income()
            elif choice == "0":
                print("Tot ziens! 👋")
                break
            else:
                print("Ongeldige keuze.")