# https://ru.hexlet.io/challenges/python_functions_count_by_years
# https://ru.hexlet.io/code_reviews/435304

# Python: Функции → Счётчик одногодок
# Реализуйте функцию get_men_counted_by_year(), которая принимает на вход
# список пользователей и возвращает словарь, в котором ключ — это год рождения,
# а значение — количество мужчин, родившихся в этот год.


import collections


def get_men_counted_by_year(data):
    men_filtered = filter(lambda entry: entry['gender'] == 'male', data)
    years = map(lambda entry: int(entry['birthday'][:4]), men_filtered)
    return dict(collections.Counter(years))


users = [
    {'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
    {'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
    {'name': 'Eiegon', 'gender': 'male', 'birthday': '1963-11-03'},
    {'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
    {'name': 'Robb', 'gender': 'male', 'birthday': '1980-05-14'},
    {'name': 'Tisha', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Rick', 'gender': 'male', 'birthday': '2012-11-03'},
    {'name': 'Joffrey', 'gender': 'male', 'birthday': '1999-11-03'},
    {'name': 'Edd', 'gender': 'male', 'birthday': '1973-11-03'},
]


print(get_men_counted_by_year(users))
assert get_men_counted_by_year(users) == {1973: 3, 1963: 1, 1980: 2, 2012: 1, 1999: 1}
