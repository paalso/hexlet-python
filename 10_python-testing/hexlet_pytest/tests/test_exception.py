import pytest
from hexlet_pytest.exception import function_with_exception


def test_regular():
    assert function_with_exception(2) == 26


# плохой способ:
# Если функция function_with_exception() не выбросит исключение, то тест
# пройдет, потому что код не попадет в блок except
def test_exception_bad():
    try:
        function_with_exception(0)
    except Exception as e:
        # assert type(e) == ZeroDivisionError
        assert type(e) == ValueError


# правильный способ
def test_exception():
    with pytest.raises(ValueError) as e:
        function_with_exception(0)

    assert str(e.value) == 'Arg is 0'
