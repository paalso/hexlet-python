#!/usr/bin/env python3

# Python: Объектно-ориентированный дизайн 
# 17. Множественное наследование и миксины 

'''
EqualityMixin реализует метод __eq__ и позволяет сравнить два экземпляра
одного класса. Если аттрибуты экземляров равны, то они считаются равными.

SerializeMixin реализует методы:
    serialize возвращает сериализованное представление объекта в JSON
    deserialize принимает JSON и создает новый объект из него
'''

from mixins import SerializeMixin, EqualityMixin
from classes import User as BaseUser


# расширим наш класс User миксиной
class User(BaseUser, EqualityMixin):
    pass


class UserPro(BaseUser, SerializeMixin, EqualityMixin):
    pass


def check_EqualityMixin():
    u1 = User('Mike', 'mike@mail.com', 'password1')
    u2 = User('Mike', 'mike@mail.com', 'password1')
    u3 = User('Alice', 'alice@mail.com', 'password1')

    assert u1 == u2  # True
    assert u1 != u3  # False
    u4 = BaseUser('Mike', 'mike@mail.com', 'password1')

    # миксина позволяет сравнивать лишь экземпляры одного и того же класса
    assert u1 != u4  # False


def check_SerializeMixin():
    u1 = UserPro('Mike', 'mike@mail.com', 'password')
    data = u1.serialize()
    print(data)

    # метод deserialize должен возвращать новый объект
    u2 = UserPro.deserialize(data)
    print(u2)
    print(type(u2))
    print(u2.__dict__)

    # аттрибуты равны
    assert u1 == u2     # True

    # но объект создается новый
    assert not (u1 is u2)   # False


def main():
    check_EqualityMixin()
    check_SerializeMixin()


if __name__ == '__main__':
    main()
