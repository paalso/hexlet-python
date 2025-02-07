# https://ru.hexlet.io/courses/python-advanced-testing/lessons/stub/exercise_unit
# https://ru.hexlet.io/code_reviews/1178768

# Python: Продвинутое тестирование
# 7. Тестирование HTTP-запросов

'''
Протестируйте функцию get_user_main_language(user_name, client), которая
определяет язык, на котором пользователь создал больше всего репозиториев.

Для реализации этой задачи функция get_user_main_language() выполняет запрос
к веб-сервису при помощи клиента client. Этот клиент извлекает все репозитории
указанного пользователя по первому параметру user_name. Каждый репозиторий в
этом списке содержит указание основного языка репозитория. Эта информация
используется для поиска того языка, который используется чаще. Если список
репозиториев пуст, функция возвращает None. Замените клиент тестовым двойником:

Т.е. тестируемая функция устроена так, что где-то внутри себя (!!!) получает
от client с помощью метода client.list_for_users
список информации о репозиториях в определенном формате:
client.list_for_usersuser_name) -> [{ "language": "php", ... }, { "language": "javascript", ... }, ...]
и нужно имитировать некий клиент FakeClient, который бы обеспечивал такой интерфейс
'''

class FakeClient:
    def __init__(self, data):
        self.data = data

    def list_for_users(self, user_name):
        return self.data
       

from fake_client import FakeClient
from functions import get_function

get_user_main_language = get_function()


def test_get_user_main_language():
    data = [{ "language": "php" }, { "language": "js" }, { "language": "js" }]
    client = FakeClient(data)
    most_used_language = get_user_main_language("hexlet", client)
    assert most_used_language ==  "js"

    data = []
    client = FakeClient(data)
    most_used_language = get_user_main_language("hexlet", client)
    assert most_used_language is None


# BEGIN (write your solution here)
def test_get_user_main_language():
    data = [
        {'language': 'php'},
        {'language': 'java'},
        {'language': 'java'},
        {'language': 'php'},
        {'language': 'php'},
        {'language': 'c'},
    ]
    client = FakeClient(data)
    assert get_user_main_language('hard_working_programmer', client) == 'php'


def test_get_user_main_language_with_empty():
    data = []
    client = FakeClient(data)
    assert get_user_main_language('lazy_programmer', client) is None
# END

