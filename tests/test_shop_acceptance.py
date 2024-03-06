import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)

from inventory import Shop, Item 
from discount_manager import DiscountManager 
from tests.exceptions import (ItemNotFoundError, NegativeInventoryError, DuplicateIdError, InvalidDiscountError, IdNotInStockError)
class TestComicShopAcceptance(unittest.TestCase):
    
    def setUp(self):
        self.shop = Shop("Store")
        self.item1 = Item("Bread", "Bakery", "11111", 7.99, 3)
        self.shop.add_item(self.item1)

    def test_user_flow(self):
        #А1
        found_items = self.shop.get_items_by_title("Bread")
        self.assertEqual(len(found_items), 1)

        #И2
        discount_manager = DiscountManager(self.shop)
        discount_manager.define_discount("11111", 25)
        item_with_discount = self.shop.get_items_by_id("11111")[0]
        self.assertAlmostEqual(item_with_discount.price, 5.99, places=2)

        #И1
        self.shop.sell_item(item_with_discount)
        self.assertEqual(item_with_discount.inventory_count, 2)

if __name__ == '__main__':
    unittest.main()
