# https://ru.hexlet.io/challenges/python_functions_typechecked_functions_exercise/instance

# Python: Функции с проверкой типов

'''
Написать пару декораторов, выполняющих проверку типов аргументов согласно их
(аргументов) аннотациям. Если при вызове функции тип какого-либо значения не
соответствует указанному в аннотации типу аргумента, обёрнутая функция не
должна быть вызвана - декоратор должен вернуть соответствующую ошибку.

Уточняю несколько моментов:
    Функция typecheck() останавливает выполнение (и проверку) на первой ошибке
    типизации
    Функция typecheck_all() проверяет все аргументы, накапливая ошибки, и лишь
    потом останавливает выполнение, если ошибки были;
    Обе функции оборачивают только функции, принимающие именованные аргументы
    Аннотации должны быть простыми типами, чтобы можно было проверить
    соответствие типа с помощью вызова isinstance(value, some_type)

    Постарайтесь выразить typecheck_all() через typecheck(). Это непросто,
    но интересно!
'''

from functools import wraps


def format_error(error):
    """Format type violation message."""
    argument, value, expected_type = error
    return (
        f'Bad argument type for argument "{argument}":'
        f' {type(value)} instead of {expected_type}'
    )


def throw_error(*args):
    """Raise one typing violation."""
    raise TypeError(format_error(args))


def throw_errors(errors):
    """Raise one error for all typing violations."""
    raise TypeError('\n'.join(map(format_error, errors)))


def check_argument(argument, types):
    if isinstance(types, tuple):
        return any(map(lambda t: isinstance(argument, t), types))
    return isinstance(argument, types)


def typecheck(error_callback=throw_error):
    """
    Добавляет к функции предусловие, проверяющие типы аргументов.

    Проверка типов делается на основе аннотаций, указанных в сигнатуре
    оборачиваемой функции.

    Arguments:
        error_callback - функция, получающая информацию об ошибке типизации.
        Функция принимает имя аргумента, значение и ожидаемый тип.
        Обычно error_callback ничего не возвращает, а вместо этого возбуждает
        исключение (см. реализацию по умолчанию - throw_error).

    Returns:
        Декоратор, добавляющий проверку типов к функции.

    """
    # BEGIN (write your solution here)
    def wrapper(func):
        annotations = func.__annotations__

        @wraps(func)
        def inner(**kwargs):
            for arg, value in kwargs.items():
                expected_type = annotations[arg]
                if not check_argument(value, expected_type):
                    error_callback(arg, value, expected_type)
            result = func(**kwargs)
            return result
        return inner
    return wrapper
    # END


def typecheck_all(error_callback=throw_errors):
    """
    Добавляет к функции предусловие, проверяющие типы аргументов.

    Проверка типов делается на основе аннотаций, указанных в сигнатуре
    оборачиваемой функции.

    Arguments:
        error_callback - функция, получающая информацию об ошибке типизации.
        Функция принимает список кортежей, описывающих все ошибки типизации.
        Каждый кортеж содержит имя аргумента, значение и ожидаемый тип.
        Обычно error_callback ничего не возвращает, а вместо этого возбуждает
        исключение (см. реализацию по умолчанию - throw_errors).

    Returns:
        Декоратор, добавляющий проверку типов к функции.

    """
    # BEGIN (write your solution here)
    def wrapper(func):
        annotations = func.__annotations__

        @wraps(func)
        def inner(**kwargs):
            errors = []
            for arg, value in kwargs.items():
                expected_type = annotations[arg]
                if not check_argument(value, expected_type):
                    errors.append((arg, value, expected_type))
            if errors:
                error_callback(errors)
            result = func(**kwargs)
            return result
        return inner
    return wrapper
    # END


def test_typecheck():
    errors = []

    @typecheck(lambda *args: errors.append(args))
    def int_and_str(i: int, s: str):
        return (i, s)

    errors[:] = []  # очищаем список
    assert int_and_str(i=0, s='') == (0, '')
    assert errors == []

    errors[:] = []
    assert int_and_str(i='foo', s='bar') == ('foo', 'bar')
    assert errors == [('i', 'foo', int)]

    errors[:] = []
    assert int_and_str(i=1, s=2) == (1, 2)
    assert errors == [('s', 2, str)]


def test_typecheck_all():
    errors = []

    @typecheck_all(lambda arg: errors.append(arg))
    def int_and_str(i: int, s: str):
        return (i, s)

    assert int_and_str(i='x', s=10) == ('x', 10)
    assert errors == [
        [('i', 'x', int), ('s', 10, str)],  # один список из двух ошибок
    ]


if __name__ == '__main__':
    # @typecheck_all()
    # def multiply(times: int, value: (str, tuple)):
    #     return value * times

    # print(multiply(times=10, value='1'))
    # print(multiply(times=10, value=(42,)))
    # print(multiply(times='12', value=(42,)))
    # print(multiply(times=12, value=None))

    # оба аргумента — не того типа
    # print(multiply(times='12', value=None))

    # errors = []

    # @typecheck(lambda *args: errors.append(args))
    # def int_and_str(i: int, s: str):
    #     return (i, s)

    # print(int_and_str(i='foo', s='bar'))
    # print(errors)

    test_typecheck()
    test_typecheck_all()
