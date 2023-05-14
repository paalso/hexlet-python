# https://ru.hexlet.io/challenges/python_basics_invert_case_exercise/instance

# Основы Python. Испытание → Необязательные параметры функций
# =================================================

# Реализуйте функцию invert_case(), которая меняет в строке регистр каждой
# буквы на противоположный.


def invert_case(text):
    return ''.join(c.upper() if c.islower() else c.lower() for c in text)


assert invert_case('Hello, World!') == 'hELLO, wORLD!'
assert invert_case('I love Python') == 'i LOVE pYTHON'
