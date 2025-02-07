# https://ru.hexlet.io/courses/python-lists/lessons/slices/exercise_unit

# Python: Списки → Срезы
# =======================

# Реализовать две функции — rotated_left и rotated_right. Каждая функция должна

# - принять список, кортеж или строку в качестве аргумента,
# - с помощью срезов и конкатенации получить новое значение того же типа,
# - вернуть это значение.


def rotated_left(items):
    return items[1:] + items[:1]


def rotated_right(items):
    return items[-1:] + items[:-1]


L = [1, 2, 3, 4]
print(L)
print(rotated_left(L))
print(rotated_right(L))

s = "abcde"
print(s)
print(rotated_left(s))
print(rotated_right(s))

'''
def rotate(items):
    if items:
        items.insert(0, items.pop(-1))
'''