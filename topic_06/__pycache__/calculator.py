import re
from operations import div, mult, sum, min
def get_number(prompt):
    while True:
        number = input(prompt)
        if re.match(r"^[0-9]+\.?[0-9]*$", number):
            return float(number)
        else:
            print("Невірний формат числа. Спробуйте ще раз.")

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


if __name__ == "__main__":
    main()
