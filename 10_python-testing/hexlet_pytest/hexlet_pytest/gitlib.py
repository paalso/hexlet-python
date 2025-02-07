#!/usr/bin/env python3

# Библиотека для работы с GitHub API
from github import Github

GITHUB_TOKEN = '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'


def get_private_fork_names(username, client=None):
    if not client:
        client = Github(GITHUB_TOKEN)
    # Клиент выполняет запрос на GitHub и возвращает
    # список приватных репозиториев указанной организации
    repos = client.get_user(username).get_repos(type='private')
    # Оставляем только имена приватных форков
    return [repo.name for repo in repos if repo.fork]


def main():
    # print(dir(Github))
    client = Github(GITHUB_TOKEN)
    print(client)
    print(type(client))


if __name__ == '__main__':
    main()


'''
>>> from tests.github_fake import GithubFake
>>> from github import Github
>>> GITHUB_TOKEN = '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'
>>> client = Github(GITHUB_TOKEN)
>>> client
<github.MainClass.Github object at 0x7f19e07c2500>
>>> type(client)
<class 'github.MainClass.Github'>

>>> username = 'paalso'
>>> user = client.get_user(username)
>>> user
NamedUser(login="paalso")
>>> type(user)
<class 'github.NamedUser.NamedUser'>

>>> private_repos = client.get_user(username).get_repos(type='private')
>>> private_repos
<github.PaginatedList.PaginatedList object at 0x7f19e07c2440>

>>> L = list(private_repos)
>>> len(L)
39
>>> repo0 = L[0]
>>> repo0
Repository(full_name="paalso/a-plus")
>>> repo0.fork
False

>>> repo19 = L[19]
>>> repo19
Repository(full_name="paalso/lab6")
>>> repo19.fork
True

>>> private_repos_names = [repo.name for repo in private_repos]
>>> private_repos_names
['a-plus', 'alien_invasion', 'bash-basics', 'catch-ball', 'cs50',
'eloquent_js', 'github-slideshow', 'grannys_crop', 'hexlet-git', 'hexlet-js',
'hexlet-python', 'hexlet_layout_design', 'hse_python_course', 'hse_statda',
'itmo_webdev_challenges', 'itmo_webdev_project', 'js_way',
'kernighan_ritchie', 'kinomonster', 'lab6', 'layout-designer-project-lvl1',
'learning_with_python', 'lexi', 'lunar_mare', 'mipt_python_course',
'mit_6.00.1x', 'motion_landing', 'myandex_murrrket',
'prometheus_sample_project', 'pyramid-slide', 'python-project-lvl1',
'python-project-lvl2', 'ruby-sandbox', 'shoot_smash', 'snake',
'stepik_webdev_for_beginners', 'sweigart_automate_the_boring_stuff',
'wordpress_promo', 'zz']

>>> get_private_fork_names(username)
['lab6']

Мы должны протестировать get_private_fork_names(username, client),
которая возвращает список имен - типа:
['lab6']

client.get_user(username).get_repos(type='private') - это
github.PaginatedList.PaginatedList object,
итератор

Получается, что при написании теста мы должны знать как устроена функция 
get_private_fork_names т.к. для того чтобы создать FakeGithubClient мы
ориентируемся на строчку
repos = client.get_user(username).get_repos(type='private') внутри функции
'''
