class Person:

    def __init__(self, name, age, has_cat, eye_color, hair_color, height):
        # Присвоєння значень 
        self.name = name
        self.age = age
        self.has_cat = has_cat
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.height = height

    # Повертає опис людини

    def __str__(self):
        # Перевірка, чи має людина кота
        if self.has_cat:
            has_cat_str = "є кіт"
        else:
            has_cat_str = "немає кота"

        # Повернення текстового опису людини
        return f"Ім'я: {self.name}\nВік: {self.age}\nМає кота: {has_cat_str}\nКолір очей: {self.eye_color}\nКолір волосся: {self.hair_color}\nЗріст: {self.height}"


# Зчитує дані 

def main():
    # Введення імені 
    name = input("Введіть ваше ім'я: ")

    # Введення інформації про кота
    has_cat = input("Чи маєте ви кота? (так/ні): ")

    # Перетворення в логічний тип
    if has_cat == "так":
        has_cat = True
    elif has_cat == "ні":
        has_cat = False
    else:
        print("Неправильний ввід.")
        return

    eye_color = input("Який у вас колір очей? ")
    hair_color = input("Який у вас колір волосся? ")
    height = input("Який у вас зріст? ")

    # Створення об'єкта
    person = Person(
        name, 25, has_cat, eye_color, hair_color, height
    )

    # Вивід інформації
    print(person)


# Запуск
if __name__ == "__main__":
    main()
