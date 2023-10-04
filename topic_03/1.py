def main():
    while True:
        # Введіть перше число
        first_number = float(input("Введіть перше число: "))

        # Введіть операцію
        operation = input("Введіть операцію: ")

        # Введіть друге число
        second_number = float(input("Введіть друге число: "))

        # Перевірте, чи не ділення на нуль
        if operation == "/" and second_number == 0:
            print("Неможливо ділити на нуль!")
            continue

        # Виконайте операцію
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            result = first_number / second_number

        # Виведіть результат
        print(f"Результат: {result}")

        # Запитайте, чи хочете продовжити
        continue_calculation = input("Бажаєте продовжити? (y/n): ")
        if continue_calculation == "n":
            break


if __name__ == "__main__":
    main()
