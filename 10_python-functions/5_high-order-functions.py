# https://ru.hexlet.io/courses/python-functions/lessons/high-order-functions/exercise_unit
# Python: Словари и Множества → Функции высшего порядка

# Реализовать функцию call_twice, которая должна
# - принять функцию и произвольный набор аргументов для неё,
# - вызвать функцию с заданными аргументами дважды,
# - вернуть пару из результатов вызовов (первый, затем второй).


def push_and_count(target, *, value):
    target.append(target)
    return len(target)


def call_twice(fun, *args, **kwargs):
    first_result = fun(*args, **kwargs)
    second_result = fun(*args, **kwargs)
    return (first_result, second_result)


x = call_twice(input, 'Enter value: ')
print(x)

x = call_twice(call_twice(push_and_count, [], value=42))
print(x)
