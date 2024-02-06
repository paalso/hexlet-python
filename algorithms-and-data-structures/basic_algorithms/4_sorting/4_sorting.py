#!/usr/bin/env python3

# https://ru.hexlet.io/courses/basic-algorithms
# https://ru.hexlet.io/courses/basic-algorithms/lessons/sorting/exercise_unit
# https://ru.hexlet.io/code_reviews/1314853

# Основы алгоритмов и структур данных 
# 4 Алгоритмы сортировки

'''
Реализовать функцию, которая сортирует массив используя алгоритм быстрой сортировки
Функция принимает первым аргументом массив чисел, вторым направление
сортировки asc или desc по умолчанию направление равно asc.
Функция не должна мутировать исходный массив


- Выбрать из массива элемент, называемый опорным. Это может быть любой из
элементов массива или же число, вычисленное на основе значений элементов.
- Сравнить все остальные элементы с опорным и переставить их в массиве так,
чтобы разбить массив на три непрерывных отрезка, следующих друг за другом:
«меньшие опорного», «равные» и «большие».
- Для отрезков «меньших» и «больших» значений выполнить рекурсивно ту же
последовательность операций, если длина отрезка больше единицы.
'''

import time
import random


def quick_cheat_sort(item, direction='asc'):
    def inner(items):
        if len(items) <= 1:
            return items
        pivot = items[0]
        less_then_pivot = [e for e in items if e < pivot]
        greater_then_pivot = [e for e in items if e > pivot]
        equal_to_pivot = [e for e in items if e == pivot]
        return [*inner(less_then_pivot), *equal_to_pivot, *inner(greater_then_pivot)]
    
    result = inner(item)
    if direction == 'desc':
        result = result[::-1]
    return result


# Hexlet's version
def solution(items, direction='asc'):
    items_length = len(items)

    if items_length == 0:
        return []

    index = items_length // 2
    element = items[index]

    smaller_items = [
        items[i]
        for i in range(items_length)
        if items[i] < element and i != index
    ]
    bigger_items = [
        items[i]
        for i in range(items_length)
        if items[i] >= element and i != index
    ]

    sorted_smaller_items = solution(smaller_items, direction)
    sorted_bigger_items = solution(bigger_items, direction)

    if direction == 'asc':
        return [*sorted_smaller_items, element, *sorted_bigger_items]
    return [*sorted_bigger_items, element, *sorted_smaller_items]


def measure_time(tries):
    def wrapper(func):
        start_time = time.time()
        def inner(*args, **kwargs):
            for i in range(tries):
                result = func(*args, **kwargs)
            duration = time.time() - start_time
            print(f'Duration of {tries} tries of function {func.__name__}: ' +
                  f'is {duration :<.2f} seconds')
            return result
        return inner
    return wrapper


def main():
    tries = 500
    array_size = 10_000
    array = [random.randint(1, 1000) for i in range(array_size)]

    measure_time(tries)(quick_cheat_sort)(array)
    measure_time(tries)(solution)(array)

    measure_time(tries)(quick_cheat_sort)(array, 'desc')
    measure_time(tries)(solution)(array, 'desc')


if __name__ == '__main__':
    main()


# Results:
# $ python3 4_sorting.py 
# Duration of 500 tries of function quick_cheat_sort: is 3.44 seconds
# Duration of 500 tries of function solution: is 11.26 seconds
# Duration of 500 tries of function quick_cheat_sort: is 3.31 seconds
# Duration of 500 tries of function solution: is 11.06 seconds
