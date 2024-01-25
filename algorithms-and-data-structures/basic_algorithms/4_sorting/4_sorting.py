#!/usr/bin/env python3

# https://ru.hexlet.io/courses/basic-algorithms
# https://ru.hexlet.io/courses/basic-algorithms/lessons/sorting/exercise_unit
# https://ru.hexlet.io/code_reviews/?????????

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


def get_partitions(items, left_id, right_id):

    left_pivot_id = (left_id + right_id) // 2
    right_pivot_id = left_pivot_id
    pivot = items[left_pivot_id]

    while True:
        while items[left_id] < pivot:
            left_id += 1

        while items[right_id] > pivot:
            right_id -= 1

        if left_pivot_id <= left_id and right_id <= right_pivot_id:
            return (left_pivot_id, right_pivot_id)

        if items[left_id] == pivot:
            left_pivot_id -= 1
            items[left_pivot_id], items[left_id] == items[left_id], items[left_pivot_id]
        else:
            right_pivot_id += 1
            items[right_pivot_id], items[left_id] == items[left_id], items[right_pivot_id]

        if items[right_id] == pivot:
            right_pivot_id += 1
            items[right_pivot_id], items[right_id] == items[right_id], items[right_pivot_id]
        else:
            left_pivot_id -= 1
            items[left_pivot_id], items[right_id] == items[right_id], items[left_pivot_id]


L = [1, 2, 6, 5, 2, 6, 9, 1, 6, 8]
print(f'Before:\n', *L)

get_partitions(L, 0, len(L) - 1)
print(f'After:\n', *L)
