# https://ru.hexlet.io/courses/python-functions/lessons/high-order-functions/exercise_unit
# Функции высшего порядка

# реализовать функцию call_twice, которая должна
# - принять функцию и произвольный набор аргументов для неё,
# - вызвать функцию с заданными аргументами дважды,
# - вернуть пару из результатов вызовов (первый, затем второй).


def push_and_count(target, *, value):
    target.append(target)
    return len(target)


def shoot():
    return 'Bang!'


def call_twice(func, *args, **kwargs):
    result1 = func(*args, **kwargs)
    result2 = func(*args, **kwargs)
    return result1, result2


x1 = call_twice(input, 'Enter value: ')    # ok
print(x1)

x2 = call_twice(shoot)     # ok
print(x2)

y = call_twice(push_and_count, [], value=42)
print(y)
