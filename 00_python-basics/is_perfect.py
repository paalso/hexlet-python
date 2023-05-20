# https://ru.hexlet.io/challenges/python_basics_perfect_numbers_exercise/instance

# Основы Python. Испытание → Совершенное число
# ============================================

# Реализуйте функцию is_perfect(), которая принимает число и возвращает True,
# если оно совершенное, и False — в ином случае.
# Совершенное число — это положительное целое число, равное сумме его
# положительных делителей (не считая само число).

import random


def sum_of_divisors(number: int) -> int:
    sum_ = 0
    half_number = number // 2
    for k in range(1, half_number + 1):
        if number % k == 0:
            sum_ += k
    return sum_


def is_perfect(number: int) -> bool:
    return number > 0 and sum_of_divisors(number) == number


perfect_numbers = (6, 28, 8128, 33550336)

for n in perfect_numbers:
    assert is_perfect(n)

for _ in range(5):
    number = random.randint(-100_000, 100_000)
    if number in perfect_numbers:
        continue
    assert not is_perfect(number)
