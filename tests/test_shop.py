import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)
from main import Item

class TestComicBook(unittest.TestCase):
    
    def test_comic_creation(self):
        comic = Item("Item1", "Hasbor", "11111", 7.99, 3)
        self.assertEqual(comic.title, "Item1")
        self.assertEqual(comic.manufacturer, "Hasbor")
        self.assertEqual(comic.id, "11111")
        self.assertEqual(comic.price, 7.99)
        self.assertEqual(comic.inventory_count, 3)

# запустить тесты
if __name__ == '__main__':
    unittest.main()
