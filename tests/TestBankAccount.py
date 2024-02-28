import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)

from BankAccount import BankAccount
from User import User


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.user = User("Ivan")
        self.account = BankAccount(self.user)
        
if __name__ == '__main__':
    unittest.main()

