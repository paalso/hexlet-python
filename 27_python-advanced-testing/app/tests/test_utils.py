from src.utils import build_user, for_each, Sqrer
from schema import Schema
from unittest.mock import Mock


preset_user_data = {'first_name': 'John', 'last_name': 'Doe'}
user_schema = Schema({
    'first_name': str,
    'last_name': str,
    'email': str
})


def test_build_user_schema_validity():
    random_user = build_user()
    assert user_schema.is_valid(random_user)

    preset_user = build_user(preset_user_data)
    assert user_schema.is_valid(preset_user)


def test_build_user_returns_unique_data_on_multiple_calls():
    user1 = build_user()
    user2 = build_user()
    for key in user1:
        assert user1[key] != user2[key]


def test_build_user_applies_provided_fields_correctly():
    preset_user = build_user(preset_user_data)
    assert preset_user['first_name'] == 'John'
    assert preset_user['last_name'] == 'Doe'


def test_for_each():
    mock = Mock()

    for_each([1, 2, 3], lambda v: mock(v))

    # Проверяем, что она была вызвана с правильными аргументами нужное количество раз
    assert mock.call_count == 3
    mock.assert_any_call(1)
    mock.assert_any_call(2)
    mock.assert_any_call(3)


def test_sqrer():
    mock_dependency = Mock()
    sqrer = Sqrer(mock_dependency)
    mock_dependency.get_value.return_value = 2.5
    result = sqrer.sqr()
    assert result == 6.25
