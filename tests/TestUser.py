import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)

from User import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Ivan")
    
    def test_set_password(self):
        self.user.set_password("111")
        self.assertTrue(self.user.check_password("111"))

if __name__ == '__main__':
    unittest.main()
