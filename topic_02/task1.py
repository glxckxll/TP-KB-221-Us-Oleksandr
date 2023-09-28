import math

def solve_quadratic_equation(a, b, c):
    # Обчислюємо дискримінант
    discriminant = b**2 - 4*a*c

    # Перевіряємо значення дискримінанту
    if discriminant > 0:
        # Два корені
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # Один корінь (корінь кратності 2)
        root = -b / (2*a)
        return root
    else:
        # Дискримінант від'ємний, розв'язків немає у множині дійсних чисел
        return "Розв'язків немає"

# Введення коефіцієнтів квадратного рівняння від користувача
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

# Виклик функції та виведення результату
result = solve_quadratic_equation(a, b, c)
print("Результат:", result)
