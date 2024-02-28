import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)

from inventory import Shop, Item 

class TestComicShopAcceptance(unittest.TestCase):
    
    def setUp(self):
        self.shop = Shop("Store")
        self.item1 = Item("Item1", "Hasbor", "11111", 7.99, 3)
        self.shop.add_item(self.comic1)

# запустить тесты
if __name__ == '__main__':
    unittest.main()
