# https://ru.hexlet.io/courses/python-object-oriented-design/lessons/fluent-interface/exercise_unit
# https://ru.hexlet.io/code_reviews/1135214

# Python: Объектно-ориентированный дизайн
# 6. Fluent interface

'''
Реализуйте функцию format() которая принимает на вход список городов,
производит внутри некоторые преобразования и возвращает структуру
определенного формата.
'''
from collection import Collection


def format(data):
    coll = Collection(data)
    normalized = coll.map_(normalize).unique()
    grouped_by_country = normalized.reduce_(group_by_country, {})
    splitted_and_ordered_by_countries = sorted(
        map(lambda e: (e[0], sorted(e[1])),
            grouped_by_country.all()[0].items()))
    return list(map(lambda e: {e[0]: e[1]},
                    splitted_and_ordered_by_countries))


def normalize(entry: dict) -> dict:
    return {key: val.lower().strip() for key, val in entry.items()}


def group_by_country(acc: dict, entry: dict):
    if entry['country'] not in acc:
        acc[entry['country']] = []
    acc[entry['country']].append(entry['name'])
    return acc


raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]

expected = [{'russia': ['moscow', 'samara']},
            {'turkey': ['antalia', 'istambul']},]

# format(raw).print()
print(format(raw))
