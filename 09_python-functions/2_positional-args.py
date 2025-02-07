# https://ru.hexlet.io/courses/python-functions/lessons/positional-args/exercise_unit
# https://ru.hexlet.io/code_reviews/257895

# Python: Словари и Множества → Позиционные аргументы

# Реализовать функцию greet, которая должна принимать несколько имён (как
# минимум одно!) и возвращать строку приветствия (см. примеры ниже).


def greet(name, *names):
    return "Hello, {}!".format(" and ".join((name,) + names))


assert greet('Bob') == 'Hello, Bob!'
assert greet('Moe', 'Mary') == 'Hello, Moe and Mary!'
assert greet(*'ABC') == 'Hello, A and B and C!'
