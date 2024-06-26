# https://ru.hexlet.io/courses/python-advanced-testing/lessons/side-effects/exercise_unit
# https://ru.hexlet.io/code_reviews/1165265

# Python: Объектно-ориентированный дизайн Продвинутое тестирование
# 4. Побочные эффекты 

# Протестируйте функцию, которая генерирует случайного пользователя. В этом случае пользователь — это словарь с тремя полями:
#   email
#   first_name
#   last_name
# протестировать три ситуации:
#   Вызов build_user() возвращает словарь нужной структуры
#   Каждый вызов build_user() возвращает словарь с разными данными
#   Установка свойств через параметры работает

from schema import Schema
from functions import get_function

build_user = get_function()


# BEGIN (write your solution here)
# вызов build_user() возвращает словарь нужной структуры
def test_default_build_user_schema():
    schema = Schema({
        'first_name': str,
        'last_name': str,
        'email': str
    })
    assert schema.is_valid(build_user())


# каждый вызов build_user() возвращает словарь с разными данными
def test_default_build_user_unique():
    user1 = build_user()
    user2 = build_user()
    assert user1 != user2


# установка свойств через параметры работает
def test_non_default_build_user():
    other_properties = {
        'email': 'new@email.net',
        'hobby': ['reading', 'sports']
    }
    user = build_user(other_properties)

    assert len(user) == 4
    assert user['email'] == 'new@email.net'
    assert user['hobby'] == ['reading', 'sports']
# END

# Version # 2
def test_build_user_returns_correct_structure():
    user = build_user()
    schema = Schema({
        'first_name': str,
        'last_name': str,
        'email': str,
    })
    assert schema.is_valid(user)


def test_build_user_generates_unique_users():
    user1 = build_user()
    user2 = build_user()
    assert user1 != user2


def test_build_user_with_preset_keys():
    preset_first_name = 'Paul'
    preset_email = 'paul@email.net'
    user = build_user({'first_name': preset_first_name, 'email': preset_email})
    assert user['first_name']  == preset_first_name
    assert user['email']  == preset_email


def test_build_user_with_new_preset_keys():
    hobby = ['cinema', 'sport']
    user = build_user({'hobby': hobby})
    assert user['hobby']  == hobby



