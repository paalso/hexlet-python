# https://ru.hexlet.io/courses/python-functions/lessons/recursion/exercise_unit
# https://ru.hexlet.io/code_reviews/272178

# Рекурсия
# =========
'''
Реализовать две взаимно рекурсивные функции (то есть использующие косвенную
рекурсию):
is_odd должна возвращать True, если число нечётное,
is_even должна возвращать True, если число чётное.
Для простоты считаем, что аргументы всегда будут неотрицательными.
'''


def is_odd(num):
    if num < 2:
        return bool(num)
    return is_even(num - 1)


def is_even(num):
    if num == 0:
        return True
    return is_odd(num - 1)


print(is_odd(42))   # False
print(is_odd(99))   # True
print(is_even(42))  # True
print(is_even(99))  # False
print(is_even(0))   # True
print(is_even(1))   # False
print(is_odd(0))    # False
print(is_odd(1))    # True

'''
# BEGIN
def is_odd(number):
    return False if number == 0 else is_even(number - 1)


def is_even(number):
    return True if number == 0 else is_odd(number - 1)
# END
'''