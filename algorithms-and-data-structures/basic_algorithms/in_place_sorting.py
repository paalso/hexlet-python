#!/usr/bin/env python3

# https://ru.hexlet.io/courses/basic-algorithms
# https://ru.hexlet.io/challenges/s_basic_algorithms_in_place_sorting_exercise/instance
# https://ru.hexlet.io/code_reviews/1315821

# Основы алгоритмов и структур данных 
# Испытание: O(n) cортировка
'''
Реализуйте функцию, которая сортирует массив целых чисел по следующему правилу
— сначала расставить все нечетные, а за ними все четные числа из массива.
Постарайтесь написать решение не создающее новых массивов и сложностью O(n).
'''
import random


def odd(number):
    return number % 2 == 1


def even(number):
    return number % 2 == 0


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def sort_by_parity(array):
    left = 0
    right = len(array) - 1

    while True:
        while odd(array[left]):
            left += 1
        while even(array[right]):
            right -= 1
        
        if right <= left:
            return array
        
        swap(array, left, right)


solution = sort_by_parity


def main():
    L = [random.randint(1, 10) for i in range(20)]
    result = sort_by_parity(L)
    print(result)


if __name__ == '__main__':
    main()
