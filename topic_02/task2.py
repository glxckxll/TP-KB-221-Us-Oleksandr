# Введення чисел та операції від користувача
num1 = float(input("Введіть перше число: "))
operator = input("Введіть операцію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

# Виконання операції в залежності від оператора
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    # Перевірка на ділення на нуль
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Помилка: ділення на нуль"
else:
    result = "Невідомий оператор"

# Виведення результату
print("Результат:", result)
