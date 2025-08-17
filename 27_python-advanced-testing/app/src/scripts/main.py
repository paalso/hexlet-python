from dotenv import load_dotenv
import os
from src.webutils import get_repos_full_names, get_repos
from src.utils import build_user


def build_users(count=10):
    return [build_user() for _ in range(count)]


def main():
    print(*build_users(), sep='\n')


if __name__ == "__main__":
    main()
