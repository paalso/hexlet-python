from hexlet_pytest.build_user import build_user

from schema import Schema

schema = Schema({
    'name': str,
    'age': int
})


# вызов build_user() возвращает словарь нужной структуры
def test_default_build_user_schema():
    schema = Schema({
        'first_name': str,
        'last_name': str,
        'email': str
    })
    assert schema.is_valid(build_user())


# каждый вызов build_user() возвращает словарь с разными данными
def test_default_build_user_uniqueness():
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
