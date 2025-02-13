from src.solution import custom_sort
import pytest


@pytest.fixture
def coll():
    return [3, 2, 1, 5, 4, 5]


def test_custom_sort(coll):
    assert custom_sort([]) == []
    assert custom_sort(coll) == [1, 2, 3, 4, 5, 5]
    assert custom_sort(coll, reverse=False) == [1, 2, 3, 4, 5, 5]
    assert custom_sort(coll, False) == [1, 2, 3, 4, 5, 5]
    assert custom_sort(coll, reverse=True) == [5, 5, 4, 3, 2, 1]
    assert custom_sort(coll, True) == [5, 5, 4, 3, 2, 1]
