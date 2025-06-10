from tests.fake_client import FakeClient
from src.webutils import get_user_main_language


data = [
    {'language': 'ruby'},
     {'language': 'js'},
     {'language': 'js'},
     {'language': 'ruby'},
     {'language': 'ruby'},
]
user_name = 'johndoe'


def test_get_user_main_language_non_empty_users():
    client = FakeClient(data)
    assert get_user_main_language(user_name, client=client) == 'ruby'


def test_get_user_main_language_empty_users():
    client = FakeClient([])
    assert get_user_main_language(user_name, client=client) is None
