from User import User
from BankAccount import BankAccount
import Exceptions

class App:
    def __init__(self):
        self.user = ""
        self.bank_account = ""

    def main_menu(self):
        while True:
            print("1. Создать пользователя: ")
            print("2. Внести деньги на счет: ")
            print("3. Вывести деньги со счета: ")
            print("4. Вывести баланс: ")
            print("5. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                username = input("Введите имя пользователя: ")
                password = input("Придумайте пароль: ")
                create_user(self, username, password)
                print("Пользователь создан!")
            elif choice == "2":
                if check_user(self):
                    deposit(self)
            elif choice == "3":
                if check_user(self):
                    withdraw(self)
            elif choice == "4":
                if check_user(self):
                    print(self.bank_account.get_balance())
            elif choice == "5":
                quit()

def create_user(self, username, password):
    self.user = User(username=username)
    self.user.set_password(password)
    self.bank_account = BankAccount(self.user)

def check_user(self):
    if self.user == "":
        print("Пользователь не был создан!")
    else:
        return True

def deposit(self):
    amount = input("Введите сумму для внесения: ")
    while check_num(self, amount) == False:
        amount = input("Введите сумму для внесения: ")

    password = input("Введите пароль: ")
    if self.user.check_password(password) == False:
        print("Неправильный пароль")
        quit()

    self.bank_account.deposit(float(amount))

def withdraw(self):
    amount = input("Введите сумму для вывода: ")
    while check_num(self, amount) == False:
        amount = input("Введите сумму для вывода: ")

    password = input("Введите пароль: ")
    if self.user.check_password(password) == False:
        print("Неправильный пароль")
        quit()
    try:
        self.bank_account.withdraw(float(amount))
    except Exceptions.InsufficientFunds:
        print("Недостаточно средств")

def check_num(self, num):
    try:
        num = float(num)
    except ValueError:
        return False
    
    decimal_places = len(str(num).split('.')[1])
    if decimal_places > 2:
        return False
    
    return True


if __name__ == '__main__':
    app = App()
    app.main_menu()