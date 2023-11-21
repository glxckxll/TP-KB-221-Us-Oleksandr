import datetime
import os
from calculator import Calculator
from operations import Operations

# Визначення шляху 
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")

class CalculatorApp:
    def __init__(self):
        # Ініціалізація об'єктів Calculator та Operations
        self.calculator = Calculator()
        self.operations = Operations()

    def log_action(self, action, a, b, operation, result):
        # Запис інформації про виконану операцію 
        current_time = datetime.datetime.now()
        log_message = f"{current_time}: num: a = {a}, b = {b}; operation = {operation}; result = {result}\n"
        with open(log_file_path, "a") as log_file:
            log_file.write(log_message)

    def run_calculator(self):
        while True:
            # Отримання чисел та операції
            a = self.calculator.get_number("Число a: ")
            b = self.calculator.get_number("Число b: ")
            operation = input("operation (+, -, *, /):")

            try:
                # Виконання арифметичної операції та логування 
                result = self.calculator.perform_operation(a, b, operation)
                if operation == "/":
                    self.log_action("Ділення", a, b, operation, result)
                else:
                    action_name = self.operations.get_operation_name(operation)
                    self.log_action(action_name, a, b, operation, result)

                print(f"Результат: {result}")
            except ZeroDivisionError as e:
                # Обробка помилки
                result = "Помилка: " + str(e)
                self.log_action("Ділення", a, b, operation, result)
                print(e)

            # Перевірка
            answer = input("Бажаєте продовжити? (Так Ні):")
            if answer.lower() != "так":
                break

if __name__ == "__main__":
    # Створення об'єкту CalculatorApp та запуск 
    calculator_app = CalculatorApp()
    calculator_app.run_calculator()
