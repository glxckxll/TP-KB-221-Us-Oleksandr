numbers = [7, 7, 7]

def find_insertion_point(numbers, new_number):

# Основний код
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] < new_number:
            start = mid + 1
        elif numbers[mid] > new_number:
            end = mid - 1
        else:
            return mid
    return start
 # Введення
while True:
    print("Список:", numbers)
    new_number = input("Введіть нове число, чи введіть 'Вихід', якщо хочете вийти: ")

    if new_number == 'Вихід':
        break

    new_number = int(new_number)

    insert_index = find_insertion_point(numbers, new_number)
    numbers.insert(insert_index, new_number)
