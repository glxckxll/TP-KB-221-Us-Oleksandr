import calculator
import operations


def main():
    a = calculator.get_number("Число a: ")
    b = calculator.get_number("Число b: ")
    operation = input("Операція (+, -, *, /): ")

    try:
        result = calculator.calculator(a, b, operation)
    except ZeroDivisionError as e:
        print(e)
    else:
        print(f"Результат: {result}")

    while True:
        answer = input("Бажаєте продовжити? (так/ні): ")
        if answer == "так":
            a = calculator.get_number("Число a: ")
            b = calculator.get_number("Число b: ")
            operation = input("Операція (+, -, *, /): ")

            try:
                result = calculator.calculator(a, b, operation)
            except ZeroDivisionError as e:
                print(e)
            else:
                print(f"Результат: {result}")
        else:
            break


if __name__ == "__main__":
    main()
