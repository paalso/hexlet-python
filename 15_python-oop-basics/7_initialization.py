# https://ru.hexlet.io/courses/python-oop-basics/lessons/initialization/exercise_unit

# Python: Введение в ООП -> Инициализация
# ----------------------------------------

# реализовать класс Counter. Но на этот раз счётчик будет иммутабельным
# неотрицательным целочисленным. Методы inc() и dec() должны возвращать новый
# счётчик с изменённым в большую или соответственно меньшую сторону значением
# value (по умолчанию счётчик изменяется на единицу).

# объявить в классе функцию-инициализатор, позволяющую задать начальное
# значение счётчика (атрибут value). Если же значение при инстанциировании
# не будет задано, следует принять его по умолчанию равным нулю.

# Атрибут value первоначального объекта после применения методов должен всё
# ещё содержать неизменное значение. Неизменность старого объекта и является
# условием иммутабильности.

class Counter:
    def __init__(self, value=0):
        self.value = max(value, 0)

    def inc(self, delta=1):
        return Counter(self.value + delta)

    def dec(self, delta=1):
        return Counter(self.value - delta)


def test_counter():
    c = Counter(-42)
    assert c.value == 0
    assert c.inc().inc(5).dec(2).value == 4
    assert c.inc().inc().dec().value == 1
    assert c.dec().dec().value == 0  # 0 is the minimum value
    d = c.inc(100)
    assert d.dec().value == 99
    forty_two = Counter(42)
    assert forty_two.value == 42


test_counter()
