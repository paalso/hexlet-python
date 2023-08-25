# https://ru.hexlet.io/courses/python-oop-basics/lessons/inheritance/exercise_unit
# https://ru.hexlet.io/code_reviews/355549

# Python: Введение в ООП -> Наследование
# ---------------------------------------

# Дан класс Counter, реализующий счетчик с инкрементом и декрементом.
# Реализовать класс-потомок LimitedCounter, который будет отличаться от
# Counter тем, что при инициализации будет принимать в качестве аргумента
# лимит — максимальное возможное значение счетчика.

# Требования к классу LimitedCounter:
# - Класс должен максимально использовать методы предка, если таковые
# переопределяет
# - Минимальное значение счетчика Counter — 0, должно оставаться таковым
# и для LimitedCounter


import math


class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


class LimitedCounter(Counter):
    def __init__(self, limit=math.inf):
        super().__init__()
        self.limit = limit

    def inc(self, amount=1):
        super().inc(amount)
        self.value = min(self.value, self.limit)


def test_counter():
    counter = Counter()
    counter.inc()
    counter.inc(7)
    assert counter.value == 8
    counter.dec(10)
    assert counter.value == 0
    counter.inc(7)
    counter.inc(7)
    assert counter.value == 14


def test_limitedcounter():
    counter = LimitedCounter(limit=10)
    counter.inc()
    counter.inc(7)
    assert counter.value == 8
    counter.dec(10)
    assert counter.value == 0
    counter.inc(7)
    counter.inc(7)
    assert counter.value == 10


test_counter()
test_limitedcounter()
