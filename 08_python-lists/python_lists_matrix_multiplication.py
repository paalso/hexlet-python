# https://ru.hexlet.io/challenges/python_lists_matrix_multiplication_exercise
# https://ru.hexlet.io/code_reviews/247024

# Python: Умножение матриц
# =========================
# Реализуйте функцию multiply, которая принимает две матрицы и возвращает новую
# матрицу — результат их произведения.


def multiply(matrix1, matrix2):
    common_size = len(matrix2)

    def get_xy(x, y):
        return sum(matrix1[x][i] * matrix2[i][y] for i in range(common_size))

    return [[get_xy(x, y) for y in range(len(matrix2[0]))]
            for x in range(len(matrix1)) ]


A = [[1, 2], [3, 2]]
B = [[3, 2], [1, 1]]
print(multiply(A, B))   # [[5, 4], [11, 8]]
print()

C = [[2, 5],
     [6, 7],
     [1, 8]]

D = [[1, 2, 1],
     [0, 1, 0]]
print(multiply(C, D))   # [[2, 9, 2], [6, 19, 6], [1, 10, 1]]
