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
        return sum(a, b)
    elif operation == "-":
        return min(a, b)
    elif operation == "*":
        return mult(a, b)
    elif operation == "/":
        return div(a, b)
    else:
        raise ValueError("Непідтримувана операція")

def main():
    while True:
        try:
            a = get_number("Число a: ")
            b = get_number("Число b: ")
            operation = input("Операція (+, -, *, /): ")

            if operation not in ['+', '-', '*', '/']:
                raise ValueError("Невірна операція")

            result = calculator(a, b, operation)
            print(f"Результат: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(e)

        answer = input("Бажаєте продовжити? (так/ні): ")
        if answer != "так":
            break

if __name__ == "__main__":
    main()
