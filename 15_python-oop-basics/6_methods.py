# https://ru.hexlet.io/courses/python-oop-basics/lessons/methods/exercise_unit
# https://ru.hexlet.io/code_reviews/354650

# Python: Введение в ООП -> Методы
# ---------------------------------

# Реализуйте класс Counter, представляющий собой счётчик, хранящий
# неотрицательное целочисленное значение и позволяющий это значение изменять:

# атрибут value должен хранить текущее значение счётчика (вначале равное нулю)
# метод inc() должен увеличивать текущее значение на delta единиц
# метод dec() должен уменьшать текущее значение на delta единиц


class Counter:
    value = 0

    def inc(self, delta=1):
        self.value += delta

    def dec(self, delta=1):
        self.value = max(self.value - delta, 0)


c = Counter()
c.inc()
c.inc()
c.inc(40)
assert c.value == 42
c.dec()
c.dec(30)
assert c.value == 11
c.dec(delta=100)
assert c.value == 0
