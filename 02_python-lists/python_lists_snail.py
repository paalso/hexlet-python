# https://ru.hexlet.io/challenges/python_lists_snail_exercise
# https://ru.hexlet.io/code_reviews/246458

# Python: Улитка
# ==========================
# Реализуйте функцию snail_path, которая принимает на вход матрицу и возвращает
# список элементов матрицы по порядку следования от левого верхнего элемента по
# часовой стрелке к внутреннему. Движение по матрице напоминает улитку:


def snail_path(matrix):
    h = height = len(matrix)
    if height == 0:
        return []

    w = width = len(matrix[0])
    size = height * width
    path = []
    y, x = 0, -1
    index = 1

    while True:
        while x < w - 1:
            x += 1
            path.append(matrix[y][x])
            index += 1
        if index > size: return path

        while y < h - 1:
            y += 1
            path.append(matrix[y][x])
            index += 1
        if index > size: return path

        while x > width - w:
            x -= 1
            path.append(matrix[y][x])
            index += 1
        if index > size: return path

        while y > height - h + 1:
            y -= 1
            path.append(matrix[y][x])
            index += 1
        if index > size: return path

        w -= 1
        h -= 1


print(snail_path([[1, 2, 3, 4]]))
print()

print(snail_path([[1], [2], [3], [4]]))
print()

print(snail_path([]))
print()

print(snail_path([[]]))
print()

print(snail_path([[1]]))
print()


print(snail_path([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
print()

print(snail_path([[1, 2], [3, 4]]))    # [1, 2, 4, 3]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

print(snail_path([['b', 'c', 'a'], ['3', True, 11], [None, 'foo', 0]]))
# ['b', 'c', 'a', 11, 0, 'foo', None, '3', True]
print()



# --- Version 2 ----------------------------------------

def snail_path(matrix):

    height = len(matrix)
    if not height:
        return
    width = len(matrix[0])
    if not width:
        return

    total_elements = width * height
    x, y = -1, 0
    xpadding, ypadding = 0, 0
    path = []

    while True:
        while x < width - xpadding - 1:
            x += 1
            path.append(matrix[y][x])
        if len(path) == total_elements: return path

        while y < height - ypadding - 1:
            y += 1
            path.append(matrix[y][x])
        if len(path) == total_elements: return path
        ypadding += 1

        while x > xpadding:
            x -= 1
            path.append(matrix[y][x])
        if len(path) == total_elements: return path
        xpadding += 1

        while y > ypadding:
            y -= 1
            path.append(matrix[y][x])
        if len(path) == total_elements: return path


# --- Version 3 ----------------------------------------

def rotate_left(matrix):
    return list(reversed(list(zip(*matrix))))


def snail_path(matrix):
    result = []
    while len(matrix) > 0:
        result.extend(matrix.pop(0))
        matrix = rotate_left(matrix)
    return result


# --- Version 4 (author's version) ----------------------
def rotate(matrix):
    """
    Rotate the matrix counter-clockwise.

    >>> rotate([[1]])
    [(1,)]
    >>> rotate([[1, 2, 3]])
    [(3,), (2,), (1,)]
    >>> rotate([[1, 2], [3, 4]])
    [(2, 4), (1, 3)]
    """
    return list(reversed(list(zip(*matrix))))


def snail_path(matrix):
    path = []

    def trace(submatrix):
        if not submatrix:
            return
        path.extend(submatrix[0])
        trace(rotate(submatrix[1:]))
    trace(matrix)
    return path
