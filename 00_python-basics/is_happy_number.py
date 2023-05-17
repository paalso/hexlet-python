# https://ru.hexlet.io/challenges/python_basics_happy_numbers_exercise/instance

# Основы Python. Испытание → Счастливые числа
# ============================================

# Назовем счастливыми те числа, сумма квадратов цифр которого, в результате
# ряда преобразований, превратятся в единицу. Например:
# 7   -> 7^2 = 49
# 49  -> 4^2 + 9^2 = 97
# 97  -> 9^2 + 7^2 = 130
# 130 -> 1^2 + 3^2 + 0^2 = 10
# 10  -> 1^2 + 0^2 = 1
# Реализуйте функцию is_happy_number(), которая возвращает True, если число
# счастливое, и False — если нет. Количество итераций процесса поиска
# необходимо ограничить числом 10.


def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))


def is_happy_number(number: int) -> bool:
    for _ in range(10):
        next_squares_sum = sum_of_square_digits(number)
        if next_squares_sum == 1:
            return True
        number = next_squares_sum
    return False


assert is_happy_number(7)


# BEGIN
# def is_happy_number(number):
#     for _ in range(10):
#         if number == 1:
#             return True
#         number = sum_of_square_digits(number)
#     return False
# END
