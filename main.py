from inventory import Shop, Item 
from discount_manager import DiscountManager 
from tests.exceptions import (ItemNotFoundError, InvalidDiscountError, IdNotInStockError) 

def main_menu():
    while True:
        print("\nВыберите операцию:")
        print("1. Добавить новый товар")
        print("2. Найти товар")
        print("3. Отобразить весь инвентарь")
        print("4. Отобразить доступные скидки")
        print("0. Выйти из программы")

        choice = input("Введите номер операции: ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            search_inventory_submenu()
        elif choice == "3":
            display_search_results(shop.items)
        elif choice == "4":
            discount_manager.display_discounts()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")

def add_item():
    title = input("Введите название товара: ")
    manufacturer = input("Введите производителя товара: ")
    id = input("Введите id товара: ")
    price_str = input("Введите цену товара: ")
    inventory_count_str = input("Введите количество экземпляров на складе: ")

    try:
        price = float(price_str)
        inventory_count = int(inventory_count_str)
        if price < 0 or inventory_count < 0:
            raise ValueError("Цена или количество не могут быть отрицательными.")
        new_item = Item(title, manufacturer, id, price, inventory_count) 
        shop.add_item(new_item) 
        print(f"товар '{title}' был успешно добавлен.")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        
def search_inventory_submenu():
    while True:
        print("\nВыберите операцию:")
        print("1. Искать по названию")
        print("2. Искать по производителю")
        print("3. Искать по id")
        print("4. Назад")

        choice = input("Введите номер операции: ")

        if choice == "1":
            item = search_items_by_title(shop)
            display_item_details(item)
        elif choice == "2":
            item = search_items_by_manufacturer(shop)
            display_item_details(item)
        elif choice == "3":
            item = search_item_by_id(shop)
            display_item_details(item)
        elif choice == "4":
            return
        else:
            print("Неверный выбор, попробуйте еще раз.")
            continue
        
        if item:
            item_operations_submenu(item)  



def search_items_by_title(shop):
    title = input("Введите название товара для поиска: ")
    for item in shop.items:
        if item.title.lower() == title.lower():
            return item
    print(f"товары с названием '{title}' не найдены.")
    return None

def search_items_by_manufacturer(shop):
    manufacturer = input("Введите название производителя для поиска товаров: ")
    for item in shop.items:
        if item.manufacturer.lower() == manufacturer.lower():
            return item
    print(f"Товары производителя '{manufacturer}' не найдены.")
    return None


def search_item_by_id(shop):
    id = input("Введите id товара для поиска: ")
    item = next((c for c in shop.items if c.id == id), None)
    if item is None:
        print(f"Товар с id {id} не найден.")
    return item

def display_item_details(item):
    print(f"\nНазвание: {item.title}")
    print(f"Производитель: {item.manufacturer}")
    print(f"id: {item.id}")
    print(f"Цена: {item.price}")
    print(f"Количество на складе: {item.inventory_count}\n")
    
def display_search_results(items):
    if items:
        print("Результаты поиска:")
        for item in items:
            print(f"{item.title} - {item.manufacturer} - {item.id}")
    else:
        print("товары не найдены.")


def item_operations_submenu(item):
    while True:
        print("\nВыберите операцию:")
        print("1. Продать товар")
        print("2. Удалить товар")
        print("3. Применить скидку на товар")
        print("4. Редактировать информацию о товаре")
        print("0. Назад")

        choice = input("Введите номер операции: ")

        if choice == "1":
            sell_item(item)
        elif choice == "2":
            remove_item(item)
            break
        elif choice == "3":
            if item:  
                apply_discount(item)
            else:
                print("Товар не найден.")
                break
        elif choice == "4":
            if item:  
                edit_item_info(item)
            else:
                print("Товар не найден.")
                break
        elif choice == "0":
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")


def sell_item(item):
    try:
        shop.sell_item(item)
        print(f"Товар '{item.title}' продан.")
    except IdNotInStockError as e:
        print(e)

def remove_item(item):
    try:
        shop.remove_item(item)
        print(f"Товар с id '{item.id}' удален со склада.")
    except ItemNotFoundError as e:
        print(e)

def apply_discount(item):
    discount_str = input("Введите процент скидки: ")
    try:
        discount = float(discount_str)
        if not (0 < discount <= 100):
            raise InvalidDiscountError("Процент скидки должен быть в диапазоне от 0 до 100.")
        discount_manager.define_discount(item.id, discount)  
        print(f"Скидка в размере {discount}% применена к товару '{item.title}' с id '{item.id}'.")
    except (ValueError, InvalidDiscountError) as e:
        print(e)

def edit_item_info(item):
    print(f"Редактирование информации о товаре {item.title}")
    new_title = input("Введите новое название товара: ")
    new_manufacturer = input("Введите нового производителя товара: ")
    new_price_str = input("Введите новую цену товара: ")
    
    try:
        new_price = float(new_price_str)
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        shop.edit_item_info(item, title=new_title, manufacturer=new_manufacturer, price=new_price)
        display_item_details(item)
    except ItemNotFoundError as e:
        print(e)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")

        
shop = Shop("Мой магазин")
discount_manager = DiscountManager(shop)

if __name__ == "__main__":
    main_menu()