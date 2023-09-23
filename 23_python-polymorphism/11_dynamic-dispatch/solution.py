#!/usr/bin/env python3


# https://ru.hexlet.io/courses/python-polymorphism/lessons/dynamic-dispatch/exercise_unit
# https://ru.hexlet.io/code_reviews/1155256

# Python: Полиморфизм
# 11. Динамическая диспетчеризация

from gateway import find_all_matching


def find_the_cheapest_service(data, predicates=None):
    limits = predicates or {}
    matched_hotels = find_all_matching(data, limits)
    return min(matched_hotels, key=lambda entry: entry['hotel']['cost'])


def test_with_min_max(data):
    expected = {
        'hotel': {'cost': 616, 'name': 'python_inn'},
        'service': 'kostrovok'
        }
    predicates = {'min': 600, 'max': 800}
    result = find_the_cheapest_service(data, predicates)

    assert result == expected

    expected2 = {
        'hotel': {'cost': 672, 'name': '$phpInn'},
        'service': 'kostrovok'
        }
    predicates2 = {'min': 650, 'max': 700}
    result2 = find_the_cheapest_service(data, predicates2)

    assert result2 == expected2


def main():
    import json

    with open('data.json') as f:
        data = json.loads(f.read())

    predicates = {'min': 650, 'max': 700}

    result = find_the_cheapest_service(data, predicates)
    print(result)


if __name__ == '__main__':
    main()
