# Список словників із прикладами імен та оцінок
data = [{'name': 'Anna', 'grade': 40},
        {'name': 'Peter', 'grade': 35},
        {'name': 'Michael', 'grade': 88},
        {'name': 'Ivan', 'grade': 22},
        {'name': 'Stephen', 'grade': 30},
        {'name': 'Matthew', 'grade': 55},
        {'name': 'Alexander', 'grade': 83},
        {'name': 'Boris', 'grade': 92},
        {'name': 'Rostislav', 'grade': 30},
        {'name': 'Eugene', 'grade': 75},
        {'name': 'Igor', 'grade': 100},
        {'name': 'Simon', 'grade': 92}]

# Запит від користувача про вибір ключа та напрямку сортування
parameter = input("Виберіть ключ для сортування (name або grade): ")
reverse_sort = input("Сортувати від більшого до меншого (y/n)? ").lower()

# Перевірка на вибір сортування від більшого до меншого
reverse = False
if reverse_sort == 'y':
    reverse = True

# Функція для сортування за вибраним ключем та напрямком
def sort_data(data, parameter, reverse):
    if parameter == 'name':
        return sorted(data, key=lambda x: x['name'], reverse=reverse)
    elif parameter == 'grade':
        return sorted(data, key=lambda x: x['grade'], reverse=reverse)
    else:
        print("Неправильний ключ сортування.")
        return data

# Виведення відсортованого списку
sorted_data = sort_data(data, parameter, reverse)

for item in sorted_data:
    print(f"Name: {item['name']}, Grade: {item['grade']}")
