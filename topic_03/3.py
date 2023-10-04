def test_dict_functions():
    dict = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6, 'u': 7, 'i': 8, 'o': 9, 'p': 10}

    #  Перевірка початкового стану словника
    print("Original dictionary:", dict)

    #  Додавання нового елемента в словник
    dict.update({'r': 4})
    print("update():", dict)

    #  Видалення елемента зі словника
    del dict['e']
    print("del():", dict)


    #  Повернення ключів словника
    keys = dict.keys()
    print("keys():", list(keys))

    #  Повернення значень словника
    values = dict.values()
    print("values():", list(values))

    #  Повернення кортежів (ключ, значення) словника
    items = dict.items()
    print("items():", list(items))

    #  Перевірка наявності елемента в словнику
    print("in():", 'q' in dict)

    #  Повернення довжини словника
    print("len():", len(dict))

    #  Копіювання словника
    new_dict = dict.copy()
    print("copy():", new_dict)

    #  Перевірка рівності двох словників
    print("==:", dict == new_dict)


    #  Перетворення словника в список
    list_dict = list(dict.items())
    print("list():", list_dict)

    #  Очистка словника
    dict.clear()
    print("clear():", dict)

if __name__ == "__main__":
    test_dict_functions()
