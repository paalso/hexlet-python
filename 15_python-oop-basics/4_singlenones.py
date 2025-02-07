# https://ru.hexlet.io/courses/python-oop-basics/lessons/singletones/exercise_unit

# Python: Введение в ООП -> Объекты-одиночки и глобальные перенменные
# --------------------------------------------------------------------

# Одно из применений глобального изменяемого состояния (когда таковое
# всё же применяют): глобальный реестр классов. Этот реестр позволяет
# зарегистрировать некие классы в одном месте программы, а потом
# получить доступ ко всем зарегистрированным классам в любом участке кода.

# В этом модуле находится реализация глобального реестра классов. В этот
# реестр любой класс можно добавить с помощью функции registry.add, а уже
# зарегистрированные классы можно всегда найти в словаре registry.CLASSES.
# Выглядит использование реестра так:


import registry
from foo_bar import FooBar 


class Foo:
    pass


class Cat:
    legs = 4


class Bird:
    legs = 2


registry.add(Foo)
print(registry.CLASSES)  # {'__main__.Foo': <class '__main__.Foo'>}

registry.add(FooBar)
print(registry.CLASSES)

registry.add(Cat)
registry.add(Bird)

print(registry.CLASSES)
