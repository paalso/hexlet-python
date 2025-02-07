# https://ru.hexlet.io/courses/python-object-oriented-design/lessons/modeling/exercise_unit
# https://ru.hexlet.io/code_reviews/1135088

# Python: Объектно-ориентированный дизайн
# 5. Объекты-сущности, Объекты-значения и внедренные объекты

'''
Реализовать класс Url, который позволяет извлекать из HTTP адреса,
представленного строкой, его части.

Класс должен содержать методы:
    __init__ — принимает на вход HTTP адрес в виде строки.
    get_scheme() — возвращает протокол передачи данных.
    get_hostname() — возвращает имя хоста.
    get_query_params() — возвращает параметры запроса в виде пар
    ключ-значение объекта.
    get_query_param() — получает значение параметра запроса по имени. Если
    параметр с переданным именем не существует, метод возвращает значение
    заданное вторым параметром (по умолчанию равно None).
    __eq__(self, other) — сравнивает два объекта класса Url и возвращает
    результат сравнения — True или False.
'''

from urllib.parse import urlparse, parse_qs


class Url:
    def __init__(self, url):
        self.url = url
        self.parsed_url = urlparse(url)

    def __eq__(self, other):
        return self.url == other.url

    def get_scheme(self):
        return self.parsed_url.scheme

    def get_hostname(self):
        return self.parsed_url.hostname

    def get_query_params(self):
        return parse_qs(self.parsed_url.query)

    def get_query_param(self, param, default=None):
        query_params = self.get_query_params()
        return query_params.get(param, [default])[0]


# url = Url('http://hexlet.io')
# url = Url('http://hexlet.io?key=value&key2=value2')
url = Url('http://hexlet.io:80?key=value&key2=value2')
print(url.get_scheme())
print(url.get_hostname())
print(url.get_query_params())
print(url.get_query_param('key'))           # value
print(url.get_query_param('key2', 'lala'))  # value2
print(url.get_query_param('new', 'ehu'))    # ehu
print(url.get_query_param('new'))           # None

url1 = Url('http://hexlet.io:80?key=value&key2=value2')
url2 = Url('http://hexlet.io:80?key=value')

print(url == url1)
print(url == url2)
