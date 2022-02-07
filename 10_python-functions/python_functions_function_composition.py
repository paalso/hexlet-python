# https://ru.hexlet.io/challenges/python_functions_function_composition

# Python: Функции → Композиция функций

# Реализуйте функцию compose(), которая принимает на вход две других
# одноаргументных функции и возвращает новую функцию. Эта новая функция также
# должна принимать один аргумент и применять к нему исходные функции в нужном
# порядке: для функций f и g порядок применения должен выглядеть, как f(g(x)).


def compose(f, g):
    def inner(x):
        return f(g(x))
    return inner


def add5(x):
    return x + 5


def mul3(x):
    return x * 3


assert compose(mul3, add5)(1) == 18
assert compose(add5, mul3)(1) == 8
assert compose(mul3, str)(1) == '111'
assert compose(str, mul3)(1) == '3'


"""
def compose(f, g):
    return lambda x: f(g(x))
"""
