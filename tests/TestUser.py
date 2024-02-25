import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)

from User import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Alice")
        self.user.set_password("securepassword")
    
    def test_get_username(self):
        self.assertEqual(self.user.get_username(), "Alice")
    
    def test_retrieve_password(self):
        self.assertEqual(self.user._retrieve_password(), "securepassword")

if __name__ == '__main__':
    unittest.main()
