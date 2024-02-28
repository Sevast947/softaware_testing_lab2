from exceptions import NegativeInventoryError, DuplicateIdError, ItemNotFoundError, IdNotInStockError # Импортируем исключе
class Item:
    def __init__(self, title, manufacturer, id, price, inventory_count):
        if inventory_count < 0:
            raise NegativeInventoryError("Количество экземпляров товара не может быть отрицательным.")
        self.title = title
        self.manufacturer = manufacturer
        self.price = price
        self.id = id
        self.inventory_count = inventory_count

    def update_inventory(self, new_count):
        if new_count < 0:
            raise NegativeInventoryError("Количество экземпляров товара не может быть отрицательным.")
        self.inventory_count = new_count
        print(f"Инвентарь товара '{self.title}' обновлен: {self.inventory_count} штук.")

class Shop:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.ids = set()

    def add_item(self, item):
        if item.id in self.ids:
            raise DuplicateIdError(f"Товар с Id {item.id} уже существует в магазине.")
        self.items.append(item)
        self.ids.add(item.id)
        print(f"Товар '{item.title}' добавлен в магазин '{self.name}'.")
    
    def get_items_by_title(self, title):
        found_comics = [item for item in self.items if item.title.lower() == title.lower()]
        if not found_comics:
            raise ItemNotFoundError(f"Товары с названием '{title.lower()}' не найдены.")
        return found_comics

    def get_items_by_manufacturer(self, manufacturer):
        found_comics = [item for item in self.items if item.manufacturer.lower() == manufacturer.lower()]
        if not found_comics:
            raise ItemNotFoundError(f"Товары автора '{manufacturer.lower()}' не найдены.")
        return found_comics

    def get_items_by_id(self, id):
        found_comics = [item for item in self.items if item.id == id]
        if not found_comics:
            raise ItemNotFoundError(f"Товар с Id '{id}' не найден.")
        return found_comics
    
    def sell_item(self, item):
        if item.inventory_count <= 0:
            raise IdNotInStockError(f"Нет в наличии товара '{item.title}' для продажи.")
        item.inventory_count -= 1
        print(f"Продана одна копия товара '{item.title}'.")

    def display_inventory(self):
        print(f"Инвентарь магазина '{self.name}':")
        for item in self.items:
            print(f"Товар '{item.title}': {item.inventory_count} штук.")

    def remove_item(self, item):
        if item not in self.items:
            raise ItemNotFoundError(f"Товар '{item.title}' не найден в магазине.")
        self.items.remove(item)
        self.ids.remove(item.id)
        print(f"Товар '{item.title}' удален из магазина.")
    
    def edit_item_info(self, item, title=None, manufacturer=None, price=None):
        if item not in self.items:
            raise ItemNotFoundError(f"Товар с Id '{item.id}' не найден.")

        if title is not None:
            item.title = title

        if manufacturer is not None:
            item.manufacturer = manufacturer

        if price is not None:
            item.price = price

        print(f"Информация о Товаре с Id '{item.id}' была обновлена.")
