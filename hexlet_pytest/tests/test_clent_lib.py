from tests.fake_client import FakeClient
from hexlet_pytest.client_lib import get_user_main_language


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
