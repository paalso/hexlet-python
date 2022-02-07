# https://ru.hexlet.io/challenges/python_lists_matrix_mirroring_exercise
# https://ru.hexlet.io/code_reviews/246481

# Python: Зеркалирование матрицы
# ==========================
# Реализуйте функцию mirror_matrix, которая принимает двумерный список
# (матрицу) и изменяет его (по месту) таким образом, что правая половина
# матрицы становится зеркальной копией левой половины, симметричной относительно
# вертикальной оси матрицы. Для простоты условимся, что матрица всегда имеет
# чётное количество столбцов и количество столбцов всегда равно количеству строк.


def print_matrix(matrix):
    [print(*row) for row in matrix]


def mirror_matrix(matrix):
    def mirror_vector(vector):
        mid = len(vector) // 2
        vector[mid:] = vector[:mid + len(vector) % 2][::-1]

    [mirror_vector(row) for row in matrix]


matrix = [
    [11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [31, 32, 33, 34, 35, 36],
    [41, 42, 43, 44, 45, 46],
    [51, 52, 53, 54, 55, 56],
    [61, 62, 63, 64, 65, 66],
]

print_matrix(matrix)
print()
mirror_matrix(matrix)
print()
print_matrix(matrix)

matrix = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55],
    [61, 62, 63, 64, 65],
]

print_matrix(matrix)
print()
mirror_matrix(matrix)
print()
print_matrix(matrix)