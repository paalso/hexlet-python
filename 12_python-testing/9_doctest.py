# https://ru.hexlet.io/courses/python-testing/lessons/doctest/exercise_unit
# https://ru.hexlet.io/code_reviews/1128799

# Тестирование через документацию
# ================================

"""
Напишите doctests для функции invert_case().
Тесты должны содержать три разных кейса.
paalso: зачем три?
"""


def invert_case(string):
    '''
    Invert case

    >>> invert_case('')
    ''

    >>> invert_case('AbBa')
    'aBbA'

    >>> invert_case('AbBa1234567890!@#$%^&*()_+./>?|')
    'aBbA1234567890!@#$%^&*()_+./>?|'
    '''
    result = ''
    for char in string:
        result += char.swapcase()
    return result


if __name__ == "__main__":
    import doctest
    failed, attempted = doctest.testmod()
    assert failed == 0
    assert attempted == 3
