a = float(input("Число a: "))
b = float(input("Число b: "))

operation = (input("Операція (+, -, *, /): "))
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
match operation:
   
    case "-":
     print(f"Результат: {min(a, b)}")
     
    case "+":
     print(f"Результат: {sum(a, b)}")
     
    case "*":
     print(f"Результат:{mult(a, b)}")
      
    case "/":
     if b != 0:
      print(f"Результат: {div(a, b)}")
     
     else:
       print("Помилка")

