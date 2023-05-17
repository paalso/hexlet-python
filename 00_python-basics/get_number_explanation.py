# https://ru.hexlet.io/courses/python-basics/lessons/match/exercise_unit

# Основы Python -> Оператор Match
# ================================

# Реализуйте функцию get_number_explanation(), которая принимает на вход число
# и возвращает объяснение этого числа. Если для числа нет объяснения,
# то возвращается just a number. Объяснения есть только для следующих чисел:
# * 666 - devil number
# * 42 - answer for everything
# * 7 - prime number


def isprime(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0 or number < 2:
        return False
    upper_limit = int(number ** 0.5)
    for k in range(3, upper_limit + 1, 2):
        if number % k == 0:
            return False
    return True


def get_number_explanation(number: int) -> str:
    match number:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'


assert get_number_explanation(8) == 'just a number'
assert get_number_explanation(666) == 'devil number'
assert get_number_explanation(42) == 'answer for everything'
assert get_number_explanation(7) == 'prime number'
