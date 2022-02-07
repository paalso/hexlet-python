# https://ru.hexlet.io/challenges/python_dicts_query_string
# https://ru.hexlet.io/code_reviews/214102

# Python: Словари и Множества → Сборщик строки запроса
# =====================================================

# Query String (строка запроса) — часть URL, содержащая константы и их значения.
# Она начинается после вопросительного знака и идет до конца адреса. Пример:

# query string: page=5
# https://ru.hexlet.io/blog?page=5
# Если параметров несколько, то они отделяются амперсандом &

# query string: page=5&per=10
# https://ru.hexlet.io/blog?per=10&page=5
# 'src/solution.py'

# Напишите функцию build_query_string, которая принимает на вход словарь с
# параметрами и возвращает строку запроса, сформированную из этих параметров.


def build_query_string(params):
    return "&".join(
            ["{}={}".format(key, params[key]) for key in sorted(params)])


assert build_query_string({'per': 10, 'page': 1}) == 'page=1&per=10'
