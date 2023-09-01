# https://ru.hexlet.io/courses/python-oop-basics/lessons/exceptions/exercise_unit
# https://ru.hexlet.io/code_reviews/355555

# Python: Введение в ООП -> Исключения
# -------------------------------------

# Реализуйте декоратор suppress ("подавлять"), который должен перехватывать
# заданное исключение (одно или несколько), если таковое возникнет при вызове
# оборачиваемой функции, и возвращать вместо ошибки заданное значение
# (keyword-only аргумент "or_return", значение по умолчанию — None).

def suppress(exeptions, or_return=None):
    def wrapper(function):
        def inner(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exeptions:
                return or_return
        return inner
    return wrapper


@suppress(ZeroDivisionError, or_return=42)
def foo():
    return 1 // 0


print(foo())  # 42


@suppress((KeyError, IndexError))
def get_item(key, structure):
    return structure[key]


assert get_item(7, "foo") is None  # True
assert get_item('a', {}) is None  # True
