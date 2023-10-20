import calculator
import operations
import datetime
import os

# Визначення шляху до лог-файлу відносно поточної папки скрипта
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")

# Функція для запису дій в лог-файл
def log_action(action, a, b, operation, result):
    current_time = datetime.datetime.now()
    log_message = f"{current_time}: numbers: a = {a}, b = {b}; operation = {operation}; result = {result}\n"
    with open(log_file_path, "a") as log_file:
        log_file.write(log_message)

def main():
    while True:
        a = calculator.get_number("Number a:")
        b = calculator.get_number("Number b: ")
        operation = input("Operation (+, -, *, /):")

        try:
            if operation == "+":
                result = calculator.sum(a, b)
                log_action("Add", a, b, operation, result)
            elif operation == "-":
                result = calculator.min(a, b)
                log_action("Subtraction", a, b, operation, result)
            elif operation == "*":
                result = calculator.mult(a, b)
                log_action("Multiplication", a, b, operation, result)
            elif operation == "/":
                try:
                    result = calculator.div(a, b)
                    log_action("Division", a, b, operation, result)
                except ZeroDivisionError as e:
                    result = "Error: " + str(e)
                    log_action("Division", a, b, operation, result)
            else:
                result = "Error: unknown operation"
                log_action("Error", a, b, operation, result)

            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(e)

        answer = input("Do you wanna to continue? (Yes No):")
        if answer.lower() != "yes":
            break

if __name__ == "__main__":
    main()
