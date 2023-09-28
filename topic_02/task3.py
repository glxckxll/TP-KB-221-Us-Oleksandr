while True:
    print("Welcome to while calc")
    s = input("Знак (+, -, *, /): ")

    # Перевірка на допустимий знак операції
    if s not in ("+", "-", "*", "/"):
        print("Невірний знак операції!")
        continue

    try:
        # Введення чисел
        a = float(input("a = "))
        b = float(input("b = "))

        # Виконання операції та виведення результату
        match s:
            case "+":
                print("%.2f" % (a + b))
            case "-":
                print("%.2f" % (a - b))
            case "*":
                print("%.2f" % (a * b))
            case "/":
                if b != 0:
                    print("%.2f" % (a / b))
                else:
                    print("Ділення на нуль!")
    except ValueError:
        print("Введено невірне число. Будь ласка, введіть числа знову.")
    except ZeroDivisionError:
        print("Ділення на нуль недопустиме. Будь ласка, введіть b знову.")
    
    another_calculation = input("Бажаєте виконати ще одну операцію? (y/n): ")
    if another_calculation.lower() != "y":
        break
