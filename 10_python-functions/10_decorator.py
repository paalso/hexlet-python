# https://ru.hexlet.io/courses/python-functions/lessons/decorators/exercise_unit
# https://ru.hexlet.io/code_reviews/348646

# Декораторы
# ===========
'''
Вам предстоит реализовать декоратор, добавляющий функции мемоизацию.
Мемоизация — это запоминание уже вычисленных результатов, для уже однажды
встреченных аргументов.
Для простоты будем считать, что мемоизироваться будут численные функции одного
аргумента (аргумент — число, результат — тоже число).
'''


def memoized(func):
    memo = dict()
    def inner(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return inner


@memoized
def f(x):
##    print('Calculating...')
    return x * 10


@memoized
def g(x):
##    print('Calculating...')
    return x + 0.5


f(1)
f(1)
f(1)
print(f(1))
g(1)
print(g(1))
print(g(10))
print(memo)


# Hexlet Version
"""
def memoized(function):
    memory = {}

    def inner(argument):
        memoized_result = memory.get(argument)
        if memoized_result is None:
            memoized_result = function(argument)
            memory[argument] = memoized_result
        return memoized_result

    return inner
"""

