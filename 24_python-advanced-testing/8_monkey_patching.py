# https://ru.hexlet.io/courses/python-advanced-testing/lessons/monkey-patching/exercise_unit
# https://ru.hexlet.io/code_reviews/1180037

# Python: Продвинутое тестирование
# 8. Манкипатчинг

'''
В этом задании нужно протестировать такую же функцию
get_user_main_language(user), как и в предыдущем упражнении. Разница в том,
что здесь нужно использовать манкипатчинг, а не инверсию зависимостей.

Подмените атрибут list_for_users() в классе Client, который используется
функцией get_user_main_language(user) для отправки запроса.
'''


from client import Client
from functions import get_function

get_user_main_language = get_function()


# BEGIN (write your solution here)
def get_fake_list_for_users(username):
    data = [
        {'language': 'php'},
        {'language': 'java'},
        {'language': 'java'},
        {'language': 'php'},
        {'language': 'php'},
        {'language': 'c'},
    ]
    return data


def test_get_user_main_language():
    client = Client()
    client.list_for_users = lambda username: get_fake_list_for_users(username)
    assert get_user_main_language('hard_working_programmer', client) == 'php'


def test_get_user_main_language_with_empty():
    client = Client()
    client.list_for_users = lambda username: []
    assert get_user_main_language('lazy_programmer', client) is None
# END

