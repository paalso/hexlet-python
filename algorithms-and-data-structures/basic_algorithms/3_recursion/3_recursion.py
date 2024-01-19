#!/usr/bin/env python3

# https://ru.hexlet.io/courses/basic-algorithms/lessons/recursion/exercise_unit
# https://ru.hexlet.io/code_reviews/1270083
# https://ru.hexlet.io/code_reviews/1270469

# Основы алгоритмов и структур данных 
# 3 Рекурсия

'''
Реализуйте функцию, которая вычисляет наибольший общий делитель двух чисел
(greatest common divisor). Наибольшим общим делителем двух чисел называется
наибольшее число, на которое оба числа делятся без остатка. Для этой задачи
подойдет алгоритм Евклида.
'''

def gcd(a, b):
    if a == b:
        return a
    a, b = max(a, b), min(a, b)
    return gcd(a - b, b)


def main():
    test_data = [
        [[26, 13], 13],
        [[38, 26], 2],
        [[80, 50], 10],
        [[145, 25], 5],
        [[80, 34], 2],
        [[99, 98], 1],
    ]

    for args, answer in test_data:
        assert gcd(*args) == answer



if __name__ == '__main__':
    main()
