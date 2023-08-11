# https://ru.hexlet.io/challenges/python_functions_functional_enlarge_image_exercise/instance
# https://ru.hexlet.io/code_reviews/356872

# Python: Функции → Увеличение двумерного списка в ФП-стиле

# Реализовать функцию enlarge(), которая увеличивает переданное "изображение"
# в два раза: каждый "пиксель" удваивается по горизонтали и вертикали.
# Изображением служит список строк, а пиксели в нём — символы строк.
# Решить проблему в функциональном стиле!
# Не использовать изменяемые структуры данных, переменные, циклы и рекурсию.


import functools
import operator


def display(image):
    for line in image:
        print(line)


curry = lambda f: lambda x: lambda y: f(x, y)  # noqa: E731
compose = lambda f: lambda g: lambda x: f(g(x))  # noqa: E731

pair = lambda x: [x, x]  # noqa: E731
dup = lambda x: x + x  # noqa: E731


def enlarge(image):
    return list(
        functools.reduce(
            lambda acc, line: acc + pair(''.join(map(dup, line))),
            image, []))


glider = [' * ', '  *', '***']
enlarged_glider = ['  **  ', '  **  ', '    **', '    **', '******', '******']

display(glider)
# =>  *
# =>   *
# => ***

print()

display(enlarge(glider))
# =>   **
# =>   **
# =>     **
# =>     **
# => ******
# => ******
