import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)
from exceptions import NegativeInventoryError, DuplicateIdError, ItemNotFoundError, IdNotInStockError
from main import Item, Shop

class TestComicBook(unittest.TestCase):
    def setUp(self):
        self.shop = Shop("Shop")

        # Создаем несколько комиксов для тестирования
        self.sample_item = Item("Blanket", "Blanket factory", "12345", 5.99, 5)
        self.sample_item2 = Item("Cup", "Cup factory", "67890", 7.99, 5)

        # Добавляем комикс в магазин
        self.shop.add_item(self.sample_item)
    
    def test_item_creation(self):
        item = Item("Cup", "Cup factory", "12345", 9.99, 10)
        self.assertEqual(item.title, "Cup")
        self.assertEqual(item.manufacturer, "Cup factory")
        self.assertEqual(item.id, "12345")
        self.assertEqual(item.price, 9.99)
        self.assertEqual(item.inventory_count, 10)

    def test_negative_inventory_error(self):
        with self.assertRaises(NegativeInventoryError):
            Item("Cup", "Cup factory", "12345", 9.99, -5)

    def test_update_inventory(self):
        item = Item("Cup", "Cup factory", "12345", 9.99, 10)
        item.update_inventory(15)
        self.assertEqual(item.inventory_count, 15)

    def test_duplicate_id_error(self):
        with self.assertRaises(DuplicateIdError):
            self.shop.add_item(self.sample_item)

    def test_item_not_found_by_title_error(self):
        with self.assertRaises(ItemNotFoundError):
            self.shop.get_items_by_title("Nonexistent Title")

    def test_comic_not_found_by_author_error(self):
        with self.assertRaises(ItemNotFoundError):
            self.shop.get_items_by_manufacturer("Nonexistent Author")

    def test_comic_not_found_by_id_error(self):
        with self.assertRaises(ItemNotFoundError):
            self.shop.get_items_by_id("00000")

    def test_not_in_stock_error(self):
        with self.assertRaises(IdNotInStockError):
            self.sample_item.inventory_count = 0
            self.shop.sell_item(self.sample_item)

    def test_remove_item(self):
        self.shop.remove_item(self.sample_item)
        with self.assertRaises(ItemNotFoundError):
            self.shop.get_items_by_id(self.sample_item.id)

    def test_edit_item_info_not_found_error(self):
        with self.assertRaises(ItemNotFoundError):
            self.shop.edit_item_info(self.sample_item2)
            
    def test_edit_item_info(self):
        new_title = "Cosy Blanket"
        new_manufacturer = "Cosy factory"
        new_price = 10.99
        self.shop.edit_item_info(self.sample_item, title=new_title, manufacturer=new_manufacturer, price=new_price)
        self.assertEqual(self.sample_item.title, new_title)
        self.assertEqual(self.sample_item.manufacturer, new_manufacturer)
        self.assertEqual(self.sample_item.price, new_price)

# запустить тесты
if __name__ == '__main__':
    unittest.main()
