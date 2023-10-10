import pytest
from hexlet_pytest.gitlib import get_private_fork_names


from tests.github_fake import FakeRepo
from tests.github_fake import GithubFake
from tests.github_fake import FakeGithubClient


def test_get_private_fork_names1():
    fake_repos = [
        FakeRepo("repo1", True),
        FakeRepo("repo2", False),
        FakeRepo("repo3", True),
    ]
    client = GithubFake(fake_repos)
    result = get_private_fork_names('paalso', client=client)
    expected_result = ["repo1", "repo3"]
    assert result == expected_result


def test_get_private_fork_names2():
    # Создаем фейковый клиент
    fake_client = FakeGithubClient()

    # Вызываем функцию с фейковым клиентом
    result = get_private_fork_names("username", client=fake_client)

    # Проверяем, что результат соответствует ожидаемому списку имен
    expected_result = ["repo1", "repo3"]
    assert result == expected_result
