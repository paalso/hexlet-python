from dotenv import load_dotenv
from github import Github
import os
from src.client import Client

default_client = Client()


def get_user_main_language(user_name, client=default_client):
    data = client.list_for_users(user_name)
    if not data:
        return None

    languges = map(lambda repo: repo["language"], data)
    languages_count = {}
    for language in languges:
        if language not in languages_count:
            languages_count[language] = 1
        else:
            languages_count[language] += 1
    return max(languages_count, key=lambda k: languages_count[k])


def get_repos(token):
    client = Github(token)
    user = client.get_user()
    return user.get_repos()


def get_repos_names(token):
    client = Github(token)
    user = client.get_user()
    return [repo for repo in user.get_repos()]


def get_repos_full_names(token):
    client = Github(token)
    user = client.get_user()
    return [repo.full_name for repo in user.get_repos()]


def get_private_fork_names(username):
    load_dotenv()
    token = os.getenv('GITHUB_TOKEN')
    client = Github(token)
    repos = client.get_user(username).get_repos(type="private")
    return [repo.name for repo in repos if repo.fork]
