from src.utils import build_user
from schema import Schema


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
