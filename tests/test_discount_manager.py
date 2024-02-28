import unittest
import os
import sys
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)
from main import Item, Shop, DiscountManager

class TestComicShopIntegration(unittest.TestCase):
    def setUp(self):
        self.shop = Shop("Store")
        self.comic = Item("Item1", "Hasbor", "11111", 7.99, 3)
        self.shop.add_comic(self.comic)
        self.discount_manager = DiscountManager(self.shop)


# запустить тесты
if __name__ == '__main__':
    unittest.main()
