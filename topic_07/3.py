# Вибір ключа та напрямку сортування
parameter = input("Виберіть ключ для сортування (name або age): ").lower()
reverse_sort = input("Сортувати від більшого до меншого (y/n)? ")

# Перевірка введених даних
if parameter not in ("name", "age"):
    raise ValueError("Неправильний ключ для сортування")
if reverse_sort not in ("y", "n"):
    raise ValueError("Неправильний напрямок сортування")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student({self.name}, {self.age})"


students = [
    Student("Степан", 20),
    Student("Борис", 25),
    Student("Петро", 18),
    Student("Матвій", 22),
    Student("Ігор", 21),
    Student("Семен", 22),
    Student("Дмитро", 23),
    Student("Данило", 24),
    Student("Олександр", 17),
]


# Сортування 
if parameter == "name":
    students.sort(key=lambda student: student.name)
    if reverse_sort == "y":
        students.reverse()
elif parameter == "age":
    students.sort(key=lambda student: student.age)
    if reverse_sort == "y":
        students.sort(key=lambda student: student.age, reverse=True)


# Виведення 
for student in students:
    print(student)
