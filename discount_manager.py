from exceptions import ItemNotFoundError, InvalidDiscountError 
class DiscountManager:
    def __init__(self, shop):
        self.shop = shop
        self.discounts = {}

    def apply_discount_to_id(self, id, discount):
        item = self.shop.get_items_by_id(id)[0]
        if item:
            item.price = round(item.price * (1 - discount / 100), 2)
            print(f"Цена товара '{item.title}' со скидкой {discount}% теперь составляет {item.price}.")
        else:
            raise ItemNotFoundError(f"Товар с Id {id} не найден.")

    def define_discount(self, id, percent):
        if not (0 <= percent <= 100):
            raise InvalidDiscountError("Ошибка: скидка задана некорректно.")
        self.apply_discount_to_id(id, percent)
        self.discounts[id] = percent

    def display_discounts(self):
            if not self.discounts:  # Проверка пуст ли словарь скидок
                print("Скидок нет!")
            else:
                print("Доступные скидки:")
                for id, discount in self.discounts.items():
                    item = next((item for item in self.shop.comics if item.id == id), None)
                    if item:
                        print(f"Товар '{item.title}': {discount}% скидка.")
