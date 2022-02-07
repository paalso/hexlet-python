# https://ru.hexlet.io/courses/python-functions/lessons/closures/exercise_unit
# https://ru.hexlet.io/code_reviews/273047

# Замыкания
# ==========

# partial_apply принимает функцию от двух аргументов и первый аргумент,
# а возвращает замыкание — функцию, которая примет второй аргумент и наконец
# применит замкнутую функцию к обоим аргументам (и вернёт результат).

# flip
# Функция flip принимает в качестве единственного аргумента функцию от двух
# аргументов. Возвращаемое замыкание должно также принять два аргумента, а
# затем применить к ним замкнутую функцию, но аргументы подставить в обратном
# порядке. Таким образом flip как бы "переворачивает" ("flips") исходную функцию

def partial_apply(func, arg1):
    def inner(arg2):
        return func(arg1, arg2)
    return inner


def flip(func):
    def inner(arg1, arg2):
        return func(arg2, arg1)
    return inner


def greet(name, surname):
    return 'Hello, {name} {surname}!'.format(name=name, surname=surname)

f = partial_apply(greet, 'Dorian')
print(f('Grey'))        # 'Hello, Dorian Grey!'

f = flip(greet)
print(f('Christian', 'Teodor'))     # 'Hello, Teodor Christian!'

