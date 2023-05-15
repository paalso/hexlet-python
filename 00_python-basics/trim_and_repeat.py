# https://ru.hexlet.io/courses/python-basics/lessons/named-arguments/exercise_unit

# Основы Python -> Именованные аргументы
# ====================================

# Реализуйте функцию trim_and_repeat(), которая принимает три параметра:
#   Строку
#   offset — число символов, на которое нужно обрезать строку слева
#   repetitions — сколько раз нужно повторить строку перед возвратом
# получившейся строки

# Число символов для среза по умолчанию равно 0,
# а количество повторений по умолчанию — 1.


def trim_and_repeat(text, offset=0, repetitions=1):
    return text[offset:] * repetitions


text = 'python'


assert trim_and_repeat(text, offset=3, repetitions=2) == 'honhon'
assert trim_and_repeat(text, repetitions=3) == 'pythonpythonpython'
assert trim_and_repeat(text) == 'python'
