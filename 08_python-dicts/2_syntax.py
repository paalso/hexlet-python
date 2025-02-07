# https://ru.hexlet.io/courses/python-dicts/lessons/syntax/exercise_unit
# Python: Словари и Множества → Синтаксис

# Реализовать две функции:
# - функцию make_user, которая должна принимать два параметра — имя пользователя
# и возраст (число). Вернуть функция должна словарь с ключами 'name' и 'age', по
# которым должны быть сохранены соответствующие значения.
# - функцию format_user, которая, будучи применена к результату вызова make_user
# (помним — это словарь), должна вернуть строку вида 'Phil, 25'.

def make_user(name, age):
    return {"name": name, "age": age}


def format_user(user_info):
    return "{}, {}".format(user_info["name"], user_info["age"])


phil = make_user('Phil', 25)
print(phil)
print(format_user(phil))
