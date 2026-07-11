from dataclasses import dataclass


@dataclass
class Expense:
    amount: float
    category: str   
    description: str
    date: str

@dataclass
class Income:
    amount: float
    source: str
    description: str
    date: str