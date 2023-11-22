# Список студентів
list = [
    {"name": "Борис", "phone": "0633894436", "email": "borik@example.com", "group": "KB-221"},
    {"name": "Степан", "phone": "0947384727", "email": "stepan@example.com", "group": "KB-221"},
    {"name": "Петро", "phone": "0634329354", "email": "petro@example.com", "group": "KB-222"},
    {"name": "Олександр", "phone": "0639283964", "email": "sasshko@example.com", "group": "KB-221"},
    {"name": "Сергій", "phone": "069030283", "email": "serhii@example.com", "group": "KB-222"},
]

# Функція для виведення списку студентів
def printAllList():
    # Перебір усіх елементів списку
    for elem in list:
        # Форматування
        strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, Email is {elem['email']}, Group is {elem['group']}"
        print(strForPrint)

# Функція для додавання нового студента
def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")

    # Створення нового елементу
    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    insertPosition = 0
    # Перебір усіх елементів списку для визначення позиції
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    # Вставка нового елемента у список
    list.insert(insertPosition, newItem)
    print("New element has been added")

# Функція для видалення студента
def deleteElement():
    # Введення імені студента для видалення
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print("Element has been deleted")

# Функція для оновлення даних студента
def updateElement():
    # Введення імені
    name = input("Please enter name to be updated: ")

    # Перебір усіх елементів списку для пошуку студента
    for student in list:
        if name == student["name"]:
            phone = input("Please enter new phone: ")
            email = input("Please enter new email: ")
            group = input("Please enter new group: ")

            # Оновлення даних студента
            student["phone"] = phone
            student["email"] = email
            student["group"] = group

            print("Element has been updated")
            return
    print("Element not found")

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                updateElement()
                printAllList()
            case "D" | "d":
                deleteElement()
                printAllList()
            case "P" | "p":
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()
