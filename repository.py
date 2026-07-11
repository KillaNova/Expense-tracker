from datetime import date

class ExpensesRepository:
    def __init__(self, db):
        self.db = db

    def add(self, expense):
        self.db.cursor.execute(
            "INSTERT INTO expenses (amount, category, description, date) VALUES (?,?,?,?)",
            (expense.amount, expense.category, expense.description, expense.date)
        )
        self.db.connection.commit()

    def get_all(self):
        self.db.cursor.execute("SELECT id, amount, category, description, date FROM expenses")
        return self.db.cursor.fetchall()
    
    def delete(self, expense_id):
        self.db.cursor.execute("DELETE FROM expenses WHERE id = ?",
                               (expense_id,))
        self.db.connection.commit()
        return self.db.cursor.rowcount
    
class IncomeRepository:
    def __init__(self, db):
        self.db = db
    
    def add(self, income):
        self.db.cursor.execute(
            "INSERT INTO income (amount, source, description, date) VALUES (?,?,?,?)", (income.amount, income.source, income.description, income.date)
        )
        self.db.connection.commit()

    def get_all(self):
        self.db.cursor.execute("SELECT id, amount, source, description, date FROM income")
        return self.db.cursor.fetchall()