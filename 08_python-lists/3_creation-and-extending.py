# https://ru.hexlet.io/courses/python-lists/lessons/creation-and-extending/exercise_unit

# Python: Списки → Создание списков и добавление элементов
# =========================================================

# Реализовать две функции:
# get_square_roots
# Эта функция должна принимать число и возвращать список квадратных корней этого
# числа. Например для аргумента 9 функция должна вернуть [-3, 3]. Тест ожидает,
# что сначала в списке будет идти отрицательный корень, если таковой имеется.
# Также корень может быть и один, если аргумент равен нулю. А ещё корней может
# и не быть, если аргумент отрицательный.

# get_range
# Данная функция должна для заданного положительного числа аргумента n
# возвращать список чисел от нуля до n, не включая само число n. Если при
# вызове было передано отрицательное число или ноль, функция должна возвращать
# пустой список.

def get_square_roots(x):
    if x > 0:
        root = x ** 0.5
        return [- root, + root]
    if x == 0:
        return [0.0]
    return []


def get_range(n):
    return list(range(n))


print(get_range(5))
print(get_range(0))
print(get_range(-1))
