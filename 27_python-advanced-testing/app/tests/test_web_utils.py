import pook
from github import Github
from tests.fake_client import FakeClient
from src.client import Client
from src.webutils import (
    get_user_main_language,
    get_repos_full_names,
    get_repos_names
)


patched_list_for_users = [
    {'language': 'ruby'},
     {'language': 'js'},
     {'language': 'js'},
     {'language': 'ruby'},
     {'language': 'ruby'},
]
user_name = 'johndoe'


def test_get_user_main_language_non_empty_users1():
    client = FakeClient(patched_list_for_users)
    assert get_user_main_language(user_name, client=client) == 'ruby'


def test_get_user_main_language_empty_users():
    client = FakeClient([])
    assert get_user_main_language(user_name, client=client) is None


def test_get_user_main_language_non_empty_users2(monkeypatch):
    list_for_users = lambda self, user_name: patched_list_for_users
    monkeypatch.setattr(Client, "list_for_users", list_for_users)
    client = Client()

    assert get_user_main_language(user_name, client=client) == 'ruby'


def test_get_user_main_language_empty_users2(monkeypatch):
    list_for_users = lambda self, user_name: []
    monkeypatch.setattr(Client, "list_for_users", list_for_users)
    client = Client()

    assert get_user_main_language(user_name, client=client) is None


def test_get_repos_full_names(monkeypatch):
    class FakeUser:
        def get_repos(self):
            return [
                type("Repo", (), {"full_name": "repo1"})(),
                type("Repo", (), {"full_name": "repo2"})(),
            ]

    monkeypatch.setattr(Github, "get_user", lambda self: FakeUser())
    result = get_repos_full_names("fake-token")
    assert result == ["repo1", "repo2"]
