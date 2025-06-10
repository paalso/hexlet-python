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
