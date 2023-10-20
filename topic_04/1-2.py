import re

def get_number(prompt):
    while True:
        number = input(prompt)
        if re.match(r"^[0-9]+\.?[0-9]*$", number):
            return float(number)
        else:
            print("Невірний формат числа. Спробуйте ще раз.")

def sum(x, y):
    return x + y

def min(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ZeroDivisionError("На нуль не можна ділити")
    return x / y

def calculator(a, b, operation):

    if operation == "+":
        return sum(a,b)
    elif operation == "-":
        return min(a,b)
    elif operation == "*":
        return mult(a,b)
    elif operation == "/":
        return div(a,b)
    else:
        return "Помилка"

def main():
    a = get_number("Число a: ")
    b = get_number("Число b: ")
    operation = input("Операція (+, -, *, /): ")

    try:
        result = calculator(a, b, operation)
    except ZeroDivisionError as e:
        print(e)
    else:
        print(f"Результат: {result}")

    while True:
        answer = input("Бажаєте продовжити? (так/ні): ")
        if answer == "так":
            a = get_number("Число a: ")
            b = get_number("Число b: ")
            operation = input("Операція (+, -, *, /): ")

            try:
                result = calculator(a, b, operation)
            except ZeroDivisionError as e:
                print(e)
            else:
                print(f"Результат: {result}")
        else:
            break

if __name__ == "__main__":
    main()
