# https://ru.hexlet.io/courses/python-polymorphism/lessons/breaking-polymorphism/exercise_unit
# https://ru.hexlet.io/code_reviews/1146490

# Python: Полиморфизм
# 8. Код, который убивает полиморфизм

'''
Реализуйте функцию greet(), которая возвращает приветствие для пользователя.
Это приветствие показывается пользователю на сайте.
'''

from user import User
from guest import Guest


def greet(person):
    return person.greet()


def test_greet():
    guest = Guest()
    assert greet(guest) == 'Nice to meet you Guest!'

    user1 = User('Petr')
    assert greet(user1) == 'Hello Petr!'

    user2 = User('Anna')
    assert greet(user2) == 'Hello Anna!'

    user3 = User('Guest')
    assert greet(user3) == 'Hello Guest!'
