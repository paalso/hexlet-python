# https://ru.hexlet.io/courses/python-testing/lessons/code-coverage/exercise_unit
# https://ru.hexlet.io/code_reviews/476899


from functions import get_functions

func = get_functions()
get = func["get"]
index_of = func["index_of"]
my_slice = func["slice"]


def test_get():
    assert get([1, 2, 3], 1, "a") == 2
    assert get([4, 5, 6], 7, "val") == "val"
    assert get([7, 8, 9], 4) is None
    # BEGIN (write your solution here)
    
    # END


def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    # BEGIN (write your solution here)
    assert index_of([], 1) == -1
    assert index_of([2, 7, 3, 2, 4], 2, 1) == 3
    assert index_of([2, 7, 3, 2, 4], 2, -3) == 3
    assert index_of([2, 7, 3, 2, 4], 2, -6) == 0    # !
    assert index_of([2, 7, 3, 2, 4], 1) == -1
    # END


def test_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]
    # BEGIN (write your solution here)
    assert my_slice([1, 2, 3, 4, 5, 6], -4, -2) == [3, 4]
    assert my_slice([1, 2, 3], -4, -2) == [1]
    assert my_slice([]) == []
    
    # END
