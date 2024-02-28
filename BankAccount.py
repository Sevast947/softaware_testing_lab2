import Exceptions

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise Exceptions.InsufficientFunds("Insufficient funds")

    def get_balance(self):
        return f"Balance: {self.balance}"

    def transaction_history(self):
        return self.transactions
