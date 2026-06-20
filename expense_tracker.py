import sqlite3
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

if os.path.exists("expenses.db"):
    print("Bestand is al aangemaakt.")
else:
    print("Database klaar! Tabel 'expenses' is aangemaakt.")

