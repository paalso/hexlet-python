# https://ru.hexlet.io/challenges/python_lists_pascal_triangle_exercise
# https://ru.hexlet.io/code_reviews/207801

# Python: Треугольник Паскаля
# ============================
# Напишите функцию triangle, которая возвращает указанную строку треугольника
# Паскаля в виде массива.


def triangle(n):
    prev_row = [1]
    for i in range(n):
        next_row = [1]
        for j in range(1, i + 1):
            next_row.append(prev_row[j - 1] + prev_row[j])
        next_row.append(1)
        prev_row = next_row
    return prev_row


assert triangle(0) == [1]
assert triangle(1) == [1, 1]
assert triangle(2) == [1, 2, 1]
assert triangle(3) == [1, 3, 3, 1]
assert triangle(4) == [1, 4, 6, 4, 1]
assert triangle(5) == [1, 5, 10, 10, 5, 1]
assert triangle(7) == [1, 7, 21, 35, 35, 21, 7, 1]


"""
from operator import add


def triangle(row_number):
    row = [1]
    for _ in range(row_number):
        row = list(map(  # [x,y,z]  КРАСИВО!
            add,         # x y z 0
            row + [0],   # + + + +
            [0] + row,   # 0 x y z
        ))
    return row
"""