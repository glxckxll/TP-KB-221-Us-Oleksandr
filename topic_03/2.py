list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Виведення початкового списку
print("Original list:", list)

# Зміна порядку елементів
list.reverse()
print("reverse():", list)

# Додавання елемента на початку
list.insert(1, 1)
print("insert():", list)

# Копіювання списку
list_copy = list.copy()
print("copy():", list_copy)
# Повернення індексу елемента
print("index():", list.index(2))

# Повернення True, якщо елемент присутній у списку
print("in():", 2 in list)


# Додавання елемента на початку
list.insert(4, 1)
print("insert():", list)

# Видалення елемента
list.remove(2)
print("remove():", list)

# Розширення списку
list.extend([6, 2, 1])
print("extend():", list)

# Додавання елемента на початку
list.insert(5, 3)
print("insert():", list)

# Сортування списку
list.sort()
print("sort():", list)

# Повернення довжини списку
print("len():", len(list))

# Повернення максимального елемента
print("max():", max(list))

# Повернення мінімального елемента
print("min():", min(list))