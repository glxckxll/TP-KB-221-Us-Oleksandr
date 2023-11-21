import re
from operations import Operations

class Calculator:
    def get_number(self, prompt):
        while True:
            # Запит користувача 
            number = input(prompt)

            # Перевірка
            if re.match(r"^[0-9]+\.?[0-9]*$", number):
                return float(number)
            else:
                print("Невірний формат числа. Спробуйте ще раз.")

    def perform_operation(self, a, b, operation):
        # Створення об'єкту класу Operations
        operations = Operations()

        # Вибір відповідної арифметичної операції 
        if operation == "+":
            return operations.sum(a, b)
        elif operation == "-":
            return operations.min(a, b)
        elif operation == "*":
            return operations.mult(a, b)
        elif operation == "/":
            return operations.div(a, b)
        else:
            # Виведення повідомлення 
            return "Помилка"
