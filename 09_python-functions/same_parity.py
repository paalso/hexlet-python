# https://ru.hexlet.io/challenges/python_functions_same_parity/instance

# Python: Функции → Одинаковая чётность

# Реализуйте функцию same_parity_filter(), которая принимает на вход список и
# возвращает новый список, состоящий из элементов, у которых такая же чётность,
# как и у первого элемента исходного списка.


# Version 1
def same_parity_filter(items):
    return list(filter(lambda e: (e - items[0]) % 2 == 0, items))


# Version 2
def same_parity_filter(items):
    if len(items) == 0:
        return items

    first_element_parity = items[0] % 2
    return list(filter(lambda x: x % 2 == first_element_parity, items))


assert same_parity_filter([]) == []
assert same_parity_filter([2, 0, 1, -3, 10, -2]) == [2, 0, 10, -2]
assert same_parity_filter([-1, 0, 1, -3, 10, -2]) == [-1, 1, -3]
