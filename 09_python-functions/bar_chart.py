# https://ru.hexlet.io/challenges/python_functions_bar_chart_exercise/instance
# https://ru.hexlet.io/code_reviews/1102830

# Python: Функции → Столбчатая диаграмма
# =======================================

# Реализовать функцию, которая выводит на экран столбчатую диаграмму в виде
# строки. Функция принимает в качестве параметра последовательность чисел,
# длина которой равна количеству столбцов диаграммы. Размер диаграммы по
# вертикали должен определяться входными данными.


def barchart(data):
    chart_width = len(data)
    max_value = max(data)
    min_value = min(data)

    rows = []

    for i in range(max_value, 0, -1):
        row_tokens = [' ' if i > data[j] else '*' for j in range(chart_width)]
        rows.append(''.join(row_tokens))

    for i in range(-1, min_value - 1, -1):
        row_tokens = [' ' if i < data[j] else '#' for j in range(chart_width)]
        rows.append(''.join(row_tokens))

    return '\n'.join(rows)


# print(barchart([5, 10, -5, -3, 7]))
print()
# print(barchart([5, 0, -2, 10, 6, 1, 2, 6, 4, 8, 1, -1, 7, 3, -5, 5]))
print(barchart([3, 4, 3]))
