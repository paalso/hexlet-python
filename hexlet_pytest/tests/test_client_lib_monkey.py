from hexlet_pytest.client import Client
from hexlet_pytest.client_lib import get_user_main_language


def get_fake_list_for_users(self, username):
    data = [
        {'language': 'php'},
        {'language': 'java'},
        {'language': 'java'},
        {'language': 'php'},
        {'language': 'php'},
        {'language': 'c'},
    ]
    return data


def get_empty_fake_list_for_users(self, username):
    return []


def test_get_user_main_language():
    Client.list_for_users = get_fake_list_for_users
    client = Client()
    assert get_user_main_language('hard_working_programmer', client) == 'php'


def test_get_user_main_language_with_empty():
    Client.list_for_users = get_empty_fake_list_for_users
    client = Client()
    assert get_user_main_language('lazy_programmer', client) is None
