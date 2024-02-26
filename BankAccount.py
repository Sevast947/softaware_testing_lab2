from datetime import datetime

class Transaction:
    def __init__(self, account, date, type, amount):
        self.account = account
        self.date = date
        self.type = type
        self.amount = amount

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.history = []
    
    def deposit(self, amount):
        self.balance += amount
        self.history.append(Transaction(self, datetime.now(), "deposit", amount))
    
    def withdraw(self, amount):
        self.balance -= amount
        self.history.append(Transaction(self, datetime.now(), "withdrawal", amount))