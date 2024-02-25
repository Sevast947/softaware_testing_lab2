import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)

from BankAccount import BankAccount
from User import User


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.user = User("Bob")
        self.account = BankAccount(self.user.get_username())

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_owner_name(self):
        self.assertEqual(self.account.owner, "Bob")

if __name__ == '__main__':
    unittest.main()

