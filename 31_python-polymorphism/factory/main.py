#!/usr/bin/env python3

# https://ru.hexlet.io/code_reviews/1160077

from config_factory import ConfigFactory

def main():
    path = './fixtures/test.yml'
    config = ConfigFactory.factory(path)
    print(config.get_value('key'))


if __name__ == '__main__':
    main()
