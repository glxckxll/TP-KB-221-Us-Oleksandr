a = float(input("Число a: "))
b = float(input("Число b: "))

operation = input("Операція (+, -, *, /): ")
    #функції
def sum(x, y):
    return x + y

def min(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "На нуль не можна ділити"
    return x / y

    #обчислення
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

result = calculator(a, b, operation)

print(f"Результат: {result}")
