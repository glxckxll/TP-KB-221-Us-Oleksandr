class User:
    # Конструктор класу
    def __init__(self, name, age, car_models):
        # Присвоєння атрибутів
        self.name = name
        self.age = age
        self.car_models = car_models

    # Метод виведення інформації 
    def print_info(self):
        # Контур
        print("_" * 50)
        # Виведення інформації 
        print("Ім'я:", self.name)
        print("Вік:", self.age)
        print("Улюблені моделі машин:", ', '.join(self.car_models))
        # Контур
        print("_" * 50)


# Функція main()
def main():
    # Запит інформації 
    name = input("Введіть ім'я: ")
    age = int(input("Введіть вік: "))
    car_models = input("Введіть улюблені моделі машин через кому: ").split(",")

    # Створення об'єкта 
    user = User(name, age, car_models)

    # Виклик методу print_info() для об'єкта класу User
    user.print_info()


# Запуск
if __name__ == "__main__":
    main()