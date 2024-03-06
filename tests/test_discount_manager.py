import unittest
import io
from contextlib import redirect_stdout
import os
import sys
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)
from main import Item, Shop, DiscountManager
from tests.exceptions import ItemNotFoundError, DuplicateIdError, InvalidDiscountError

class TestComicShopIntegration(unittest.TestCase):
    def setUp(self):
        self.shop = Shop("Store")
        self.item = Item("Miror", "Glass Factory", "88888", 12.99, 5)
        self.shop.add_item(self.item)
        self.discount_manager = DiscountManager(self.shop)

    def test_duplicate_id(self):
        with self.assertRaises(DuplicateIdError):
            self.shop.add_item(self.item)
    
    def test_apply_discount_to_nonexistent_id(self):
        with self.assertRaises(ItemNotFoundError):
            self.discount_manager.apply_discount_to_id("99999", 10)

    def test_define_invalid_discount(self):
        with self.assertRaises(InvalidDiscountError):
            self.discount_manager.define_discount("88888", -10) 
        with self.assertRaises(InvalidDiscountError):
            self.discount_manager.define_discount("88888", 150) 

    def test_display_no_discounts(self):
        self.discount_manager.discounts = {}
        with io.StringIO() as buf, redirect_stdout(buf):
            self.discount_manager.display_discounts()
            self.assertEqual(buf.getvalue(), "Скидок нет!\n")

    def test_display_discounts(self):
        self.discount_manager.define_discount("88888", 10)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.discount_manager.display_discounts()
            self.assertIn("Товар 'Miror': 10% скидка.", buf.getvalue())


if __name__ == '__main__':
    unittest.main()
