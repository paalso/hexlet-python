# https://ru.hexlet.io/courses/python-object-oriented-design/lessons/fluent-interface/exercise_unit


# Python: Объектно-ориентированный дизайн
# 6. Fluent Interface

'''
Реализуйте функцию format() которая принимает на вход список городов, производит внутри некоторые преобразования и возвращает структуру определенного формата.
'''

from collection import Collection
import pprint


def format(data):
    return Collection(data). \
    map_(
        lambda e: dict((key.lower().strip(), val.lower().strip())
                       for key, val in e.items())). \
    unique(). \
    sort_by(lambda e: (e['country'], e['name'])). \
    group_by(lambda e: (e['country'], e['name'])). \
    all()
    


def main():
    raw = [{'name': 'istambul', 'country': 'turkey'},
           {'name': 'Moscow ', 'country': ' Russia'},
           {'name': 'iStambul', 'country': 'tUrkey'},
           {'name': 'antalia', 'country': 'turkeY '},
           {'name': 'samarA', 'country': '  ruSsiA'}]
    result = format(raw)
    pprint.pprint(result.all())
    expected = [{'russia': ['moscow', 'samara']},
                {'turkey': ['antalia', 'istambul']},]
    pprint.pprint(expected)
    print(result == expected)
    

if __name__ == '__main__':
    main()

