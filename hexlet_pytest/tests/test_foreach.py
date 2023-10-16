from hexlet_pytest.foreach import for_each, for_each_in_args
from unittest.mock import Mock


def test_for_each1():
    mock = Mock()
    for_each([1, 2, 3], lambda v: mock(v))

    assert mock.call_count == 3

    assert mock.call_args_list[0] == ((1,), {})
    assert mock.call_args_list[1] == ((2,), {})
    assert mock.call_args_list[2] == ((3,), {})

    print(mock.call_args_list)
    print(mock.call_args_list[0])


def test_for_each2():
    mock = Mock()
    for_each([1, 2, 3], lambda v: mock(v))

    assert1 = mock.assert_any_call(1)
    assert2 = mock.assert_any_call(2)
    assert3 = mock.assert_any_call(3)

    print(assert1, assert2, assert3)

# Неправильно !
# def test_for_each3():
#     mock = Mock()
#     for_each([1, 2, 3], lambda v: mock(v))

#     assert mock.assert_any_call(1)
#     assert mock.assert_any_call(2)
#     assert mock.assert_any_call(3)
