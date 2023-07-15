#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-functions/lessons/pure-functions/exercise_unit
# https://ru.hexlet.io/code_reviews/1080397

# Чистые функции
# ===============

# Реализуйте функцию, которая проверяет переданное число на простоту и
# печатает на экран yes или no.

def is_prime(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False

    limit = int(number ** 0.5) + 1

    for n in range(3, limit, 2):
        if number % n == 0:
            return False
    return True


def say_prime_or_not(number):
    print('yes' if is_prime(number) else 'no')


def main():
    say_prime_or_not(5) ## yes
    say_prime_or_not(4) ## no


if __name__ == '__main__':
    main()
