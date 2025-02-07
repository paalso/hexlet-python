# https://ru.hexlet.io/challenges/python_functions_horizontal_histogram_exercise/instance
# https://ru.hexlet.io/code_reviews/271687

# Python: Функции → Горизонтальная гистограмма

# Реализуйте функцию histo(), которая возвращает горизонтальную гистограмму.
# Функция принимает на вход количество бросков кубика и функцию, которая
# имитирует бросок игральной кости (её реализовывать не нужно). Вызов этой
# функции генерирует значение от 1 до 6, что соответствует одной из граней
# игральной кости.


from collections import Counter


def generate_histo_line(side, counter, token='#'):
    tokens_number = counter.get(side, 0)
    histo_line = f'{side}|{token * tokens_number}'
    if tokens_number > 0:
        histo_line = f'{histo_line} {tokens_number}'
    return histo_line


def histo(times, data_generator):
    sides = range(1, 7)
    raw_data = (data_generator() for _ in range(times))
    counter = dict(Counter(raw_data))
    histo_lines = (generate_histo_line(side, counter) for side in sides)
    return '\n'.join(histo_lines)
