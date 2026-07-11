import sqlite3

class Database:
    def __init__(self, db_name="expenses.db"):
        self.connection = sqlite3()
        self.cursor = self.connection.cursor()
        self._setup()
    
    def _setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS expenses (" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL NOT NULL, category TEXT NOT NULL, description TEXT, date TEXT NOT NULL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS income (" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL NOT NULL, category TEXT NOT NULL, description TEXT, date TEXT NOT NULL)")
        self.connection.commit()
        
