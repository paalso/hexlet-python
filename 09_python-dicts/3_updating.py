# https://ru.hexlet.io/courses/python-dicts/lessons/updating/exercise_unit
# Python: Словари и Множества → Изменение данных в словаре

# Реализовать функция count_all. Эта функция должна принимать на вход iterable
# источник и возвращать словарь, ключами которого являются элементы источника,
# а значения отражают количество повторов элемента в коллекции-источнике. Вот
# пара примеров, демонстрирующих то, как функция должна работать:


def count_all(items):
    return {e : items.count(e) for e in set(items)}


assert count_all(["cat", "dog", "cat"]) == {"cat": 2, "dog": 1}
assert count_all("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
assert count_all("*" * 20) == {'*': 20}
