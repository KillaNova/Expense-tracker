import sqlite3
from datetime import date
import os 
os.system("cls" if os.name== "nt" else "clear")



# Verbind met de database. 
# Bestaat het bestand niet? 
# Dan maakt SQLite het aan.
connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()

def setup_database():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

#----Tabel-1: Uitgaven----
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        amount      REAL NOT NULL,
        category    TEXT NOT NULL,
        description TEXT,
        date        TEXT NOT NULL   
    )
""")

#----Tabel-2: INKOMSTEN----
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,                   
        amount          REAL NOT NULL,
        category        TEXT NOT NULL,
        description     TEXT,
        date            TEXT NOT NULL
    )               
""")

connection.commit()
connection.close()



def database_exists():
    if os.path.exists("expenses.db"):
        return True
    else:
        return False
print(database_exists())

def add_expenses(amount, category, description):
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    today = date.today().isoformat()

    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (?,?,?,?)",
            (amount, category, description, today)

    )
    connection.commit()
    connection.close()
    print(f"Uitgave toegevoegd: €{amount} ({category})")

# Add expenses hier:
#
#
# ====================


def show_expenses():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("SELECT id, amount, category, description, date FROM expenses")
    expenses = cursor.fetchall()

    connection.close()

    if not expenses:
        print("Geen uitgaven gevonden.")
        return
    
    print("\n--- Alle uitgaven ---")
    for expense in expenses:
        id, amount, category, description, date = expense
        print(f"[{id}] €{amount:.2f} | {category} | {description} | {date}")


def delete_expense(expense_id):
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    
    connection.commit()
    connection.close()

    
    if cursor.rowcount > 0:
        print(f"Uitgave {expense_id} verwijderd.")
    else:
        print(f"Geen uitgave gevonden met id {expense_id}.")




def add_income (amount, source, description):
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()
    today = date.today().isoformat()

    cursor.execute(
        "INSERT INTO income (amount, source, description, date) VALUES (?,?,?,?)"
        (amount, source, description, today)    
    )
    connection.commit()
    connection.close()
    print(f"Inkomst toegevoegd: €{amount} ({source})")





MENU = """
===== EXPENSE TRACKER - ZZP ADMIN =====
UITGAVEN
1. Uitgave toevoegen
2. Uitgaven tonen
3. Uitgave verwijderen

INKOMSTEN
4. Inkomst toevoegen
5. Inkomsten tonen

FACETUREN
6. Factuur toevoegen
7. Facturen tonen
8. Factuur markeren als betaald

OVERZICHTEN
9. Winst- en verliesoverzicht
10. BTW-overzivht
11. Maandoverzicht

0. Afsluiten
=========================================

"""
# Tijdelijke placeholder voor features die nog niet af zijn

def coming_soon():
    print("Deze funcites bouwen we nog!")

def menu():
    while True:
        print("\n===== EXPENSE TRACKER — ZZP ADMIN =====")
        print(" 1. Uitgave toevoegen")
        print(" 2. Uitgaven tonen")
        print(" 3. Uitgave verwijderen")
        print(" 4. Inkomst toevoegen")
        print(" 5. Inkomsten tonen")
        print(" 6. Factuur toevoegen")
        print(" 7. Facturen tonen")
        print(" 8. Factuur markeren als betaald")
        print(" 9. Winst- en verliesoverzicht")
        print("10. BTW-overzicht")
        print("11. Maandoverzicht")
        print(" 0. Afsluiten")
        print("=======================================")
        choice = input("KEUZE: ")

        if choice == "1":
            amount = float(input("Bedrag: €"))
            category = input("Categorie: ")
            description = input("Omschrijving: ")
            add_expenses(amount, category, description)
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_expenses()
            delete_expense(int(input("Welk id verwijderen? ")))
        
        # inkomst toevoegen
        elif choice == "4":
            amount = float(input("Bedrag: €"))
            source = input("Van wie/wat? ")
            description = input("Omschrijving")
            add_income(amount, source, description)
        
        elif choice == "5":
            coming_soon()   # inkomsten tonen
        elif choice == "6":
            coming_soon()   # factuur toevoegen
        elif choice == "7":
            coming_soon()   # facturen tonen
        elif choice == "8":
            coming_soon()   # factuur betaald
        elif choice == "9":
            coming_soon()   # winst/verlies
        elif choice == "10":
            coming_soon()   # btw-overzicht
        elif choice == "11":
            coming_soon()   # maandoverzicht
        elif choice == "0":
            print("Tot ziens! 👋")
            break
        else:
            print("Ongeldige keuze.")

setup_database()
menu()