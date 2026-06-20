import sqlite3
from datetime import date
import os

# Verbind met de database. 
# Bestaat het bestand niet? 
# Dan maakt SQLite het aan.
connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()

# Maakt de tabel aan waarin we uitgaven opslaan.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    )
""")

# Slaat de wijziging op en sluit netjes af.
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


