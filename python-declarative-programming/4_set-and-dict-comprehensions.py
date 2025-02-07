# https://ru.hexlet.io/courses/python-declarative-programming/lessons/set-and-dict-comprehensions/exercise_unit
# 

# Генераторы множеств и словарей 
# =================================

# реализовать функцию number_of_unique_letters(): должна подсчитывать
# количество уникальных букв в строке-аргументе без учёта регистра:


def number_of_unique_letters(text):
    return len(set(c.lower() for c in text if c.isalpha()))


assert number_of_unique_letters("") == 0
assert number_of_unique_letters("abc") == 3
assert number_of_unique_letters("A-a-a-a-a-a!") == 1
assert number_of_unique_letters("\\(O_o)/") == 1
assert number_of_unique_letters("AaBbCcDd") == 4
