# https://ru.hexlet.io/challenges/python_dicts_find_where
# https://ru.hexlet.io/code_reviews/251149

# Python: Детектирование
# =========================

# Реализуйте функцию find_where, которая принимает на вход список книг и
# поисковый запрос и возвращает первую книгу, которая соответствует запросу.
# Каждая книга в списке — это словарь, содержащий её параметры, поисковый запрос
# — тоже словарь с параметрами.
# Если совпадений не было, то функция должна вернуть None.


def find_where(entries, filter_):

    def check_entry(entry):
        return all(
            [entry.get(key, object()) == filter_[key] for key in filter_])

    for entry in entries:
        if check_entry(entry):
            return entry


books = [
    {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
    {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
    {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
    {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
]

BOOKS = (
    {'TITLE': 'Book of Fooos', 'AUTHOR': 'Foo', 'YEAR': 1111},
    {'TITLE': 'Cymbeline', 'AUTHOR': 'Shakespeare', 'YEAR': 1611},
    {'TITLE': 'The Tempest', 'AUTHOR': 'Shakespeare', 'YEAR': 1611},
    {'TITLE': 'Book of Foos Barrrs', 'AUTHOR': 'FooBar', 'YEAR': 2222},
    {'TITLE': 'Still foooing', 'AUTHOR': 'FooBar', 'YEAR': 333},
    {'TITLE': 'Happy Foo', 'AUTHOR': 'FooBar', 'YEAR': 4444},
)

##print(BOOKS)

print(find_where(BOOKS, {}) == BOOKS[0])
print(find_where(BOOKS, {'AUTHOR': 'Pushkin'}) is None)
print(find_where(BOOKS, {'YEAR': 1111, 'AUTHOR': 'Pushkin'}) is None)
print(find_where(BOOKS, {"genre": 'Thriller'}) is None)
print(find_where(BOOKS, {"YEAR": 1111}) == {'TITLE': 'Book of Fooos', 'AUTHOR': 'Foo', 'YEAR': 1111})
print(find_where(BOOKS, {'AUTHOR': 'Shakespeare', 'YEAR': 1611})['TITLE'] == 'Cymbeline')
print(find_where(BOOKS, BOOKS[2]) == BOOKS[2])
