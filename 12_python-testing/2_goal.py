# https://ru.hexlet.io/courses/python-testing/lessons/goal/exercise_unit

# Python: Автоматическое тестирование
# ====================================

"""
Напишите тесты для функции get(collection, key, default_value). Эта функция
извлекает значение из словаря при условии, что ключ существует. В ином случае
возвращается default_value.
"""
##from functions import get_function
##get = get_function()


##def get(collection, key, default_value):
##    return collection.get(key, default_value)


if get({"hello": "world" }, "hello") != "world":
    raise Exception('Функция работает неверно!')

if get({ "hello": "world" }, "hello", "kitty") != "world":
    raise Exception('Функция работает неверно!')

if get({}, "hello", "kitty") != "kitty":
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
