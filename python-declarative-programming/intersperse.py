# https://ru.hexlet.io/challenges/python_declarative_programming_intersperse_exercise
# https://ru.hexlet.io/code_reviews/436000

# Перемежовка последовательности
# ===============================

# Реализовать функцию intersperse(), которая должна принимать два аргумента:
#  - Итерируемый источник значений
#  - Значение-разделитель
# Функция должна возвращать такой итератор, который отдавал бы
# значение-разделитель между соседними значениями из источника.

# intersperse.py

def intersperse(iterable, separator):
    if iterable:
        iter_ = iter(iterable)
        yield next(iter_)
        for item in iter_:
            yield separator
            yield item


x = intersperse([], ",")
print(x, type(x), list(x))

assert list(intersperse([], ",")) == []
assert list(intersperse([42], "foo")) == [42]
assert "".join(intersperse(["Hello", "World"], " ")) == "Hello World"
assert list(intersperse(range(4), 0)) == [0, 0, 1, 0, 2, 0, 3]


# def intersperse(items, separator):
#     if items:
#         iterator = iter(items)
#         yield next(iterator)
#         while True:
#             try:
#                 next_ = next(iterator)
#                 yield separator
#                 yield next_
#             except StopIteration:
#                 return