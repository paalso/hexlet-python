class FakeRepo:
    def __init__(self, name, fork):
        self.name = name
        self.fork = fork


# Структура этого класса описывает только ту часть,
# которая необходима для вызова client.get_user.get_repos
class GithubFake:
    # Здесь мы описываем желаемые данные, которые должны вернуться в тесте
    def __init__(self, data):
        self.data = data

    # Возвращаем сами себя, чтобы иметь возможность вызвать get_repos()
    # по цепочке
    def get_user(self, name):
        return self

    # Возвращаем переданные в начале данные
    def get_repos(self, type):
        return self.data


class FakeGithubClient:
    def get_user(self, username):
        return self

    def get_repos(self, type):
        # Возвращаем фейковые данные для тестирования
        fake_repos = [
            FakeRepo("repo1", True),
            FakeRepo("repo2", False),
            FakeRepo("repo3", True),
        ]
        return fake_repos
