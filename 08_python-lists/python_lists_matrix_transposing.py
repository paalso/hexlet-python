# https://ru.hexlet.io/challenges/python_lists_matrix_transposing_exercise
# https://ru.hexlet.io/code_reviews/214035

# Python: Транспонирование матриц
# ================================

# Реализуйте функцию transposed, которая должна принимать матрицу в виде
# списка списков и возвращать транспонированную матрицу (новый список списков).


def transposed(matrix):
    height, width = len(matrix), len(matrix[0])
    return [[matrix[j][i] for j in range(height)] for i in range(width)]


print(transposed([[1]]))    # [[1]]
print(transposed([[1, 2], [3, 4]]))     # [[1, 3], [2, 4]]
print(transposed([[1, 2], [3, 4], [5, 6]]))     # [[1, 3, 5], [2, 4, 6]]
print(transposed(transposed([[1, 2]])) == [[1, 2]])     # True


"""
def transposed(matrix):
    return list(map(list, zip(*matrix)))
"""
