import math

def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

def solve_quadratic_equation(a, b, c):
    discriminant_value = calculate_discriminant(a, b, c)
    # Розрахунок
    if discriminant_value > 0:
    # Два корені
        root1 = (-b + math.sqrt(discriminant_value)) / (2*a)
        root2 = (-b - math.sqrt(discriminant_value)) / (2*a)
        return root1, root2
    elif discriminant_value == 0:
    # Один корінь
        root = -b / (2*a)
        return root
    else:
        
        return "Розв'язків немає"

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

# Виклик функції
result = solve_quadratic_equation(a, b, c)
print("Результат:", result)
