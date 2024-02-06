#!/usr/bin/env python3

# https://ru.hexlet.io/courses/basic-algorithms
# https://ru.hexlet.io/courses/basic-algorithms/lessons/algorithm-complexity/exercise_unit
# https://ru.hexlet.io/code_reviews/1313946

# Основы алгоритмов и структур данных 
# 5 Алгоритмическая сложность

'''
Реализуйте функцию, которая проверяет является ли число простым или нет.
Оптимизируйте алгоритм так, чтобы он выполнялся за наименьшее количество итераций.
'''

import time


def measure_time(tries):
    def wrapper(func):
        start_time = time.time()
        def inner(*args, **kwargs):
            for i in range(tries):
                result = func(*args, **kwargs)
            duration = time.time() - start_time
            print(f'Duration of {tries} tries of function {func.__name__}: ' +
                  f'with args {args, kwargs} is {duration :<.2f} seconds')
            return result
        return inner
    return wrapper


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    upper_limit = int(n ** 0.5)
    
    for k in range(3, upper_limit + 1, 2):
        if n % k == 0:
            return False

    return True


def is_prime1(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    k = 3
    while k * k <= n:    
        if n % k == 0:
            return False
        k += 2
    
    return True


def is_prime2(n):
    if n < 2:
        return False
    
    upper_limit = int(n ** 0.5)
    
    for k in range(2, upper_limit + 1):
        if n % k == 0:
            return False
    return True


# Helets's version
import math


def solution(number):
    if number < 2:
        return False

    sqrt = math.sqrt(number)
    for i in range(2, int(sqrt) + 1):
        if number % i == 0:
            return False

    return True



def main():
    N = 2147483648
    tries = 1_000_000
    print(measure_time(tries)(is_prime)(N))
    print(measure_time(tries)(is_prime1)(N))
    print(measure_time(tries)(is_prime2)(N))
    print(measure_time(tries)(solution)(N))
    
    N = 87178291199
    tries = 1_000
    print(measure_time(tries)(is_prime)(N))
    print(measure_time(tries)(is_prime1)(N))
    print(measure_time(tries)(is_prime2)(N))
    print(measure_time(tries)(solution)(N))


if __name__ == '__main__':
    main()


# Results:
# Duration of 1000000 tries of function is_prime: with args ((2147483648,), {}) is 0.14 seconds
# False
# Duration of 1000000 tries of function is_prime1: with args ((2147483648,), {}) is 0.14 seconds
# False
# Duration of 1000000 tries of function is_prime2: with args ((2147483648,), {}) is 0.39 seconds
# False
# Duration of 1000000 tries of function solution: with args ((2147483648,), {}) is 0.36 seconds
# False
# Duration of 1000 tries of function is_prime: with args ((87178291199,), {}) is 5.97 seconds
# True
# Duration of 1000 tries of function is_prime1: with args ((87178291199,), {}) is 12.24 seconds
# True
# Duration of 1000 tries of function is_prime2: with args ((87178291199,), {}) is 11.52 seconds
# True
# Duration of 1000 tries of function solution: with args ((87178291199,), {}) is 11.58 seconds
# True
