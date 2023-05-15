# https://ru.hexlet.io/courses/python-basics/lessons/environment/exercise_unit

# Основы Python → Окружение
# ==========================
# Напишите функцию get_age_difference(), которая принимает два года рождения
# и возвращает строку с разницей в возрасте в виде The age difference is 11.


def get_age_difference(year1, year2):
    template = 'The age difference is '
    age_difference = abs(year1 - year2)
    return f'{template}{age_difference}'


assert get_age_difference(2001, 2018) == 'The age difference is 17'
assert get_age_difference(2018, 2001) == 'The age difference is 17'
assert get_age_difference(2018, 2018) == 'The age difference is 0'
