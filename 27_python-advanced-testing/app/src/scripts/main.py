from dotenv import load_dotenv
import os
from src.webutils import get_repos_full_names, get_repos


def main():
    load_dotenv()
    token = os.getenv('GITHUB_TOKEN')

    repos = get_repos(token)
    print(repos)
    print(get_repos_full_names(token))
    print(type(repos[0]))


if __name__ == "__main__":
    main()
