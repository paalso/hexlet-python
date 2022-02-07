#!/usr/bin/env python3

import solution
from solution import numbers1, numbers2, numbers3


def test_names():
    assert hasattr(solution, 'add')  # noqa: WPS421
    assert hasattr(solution, 'mul')  # noqa: WPS421
    assert hasattr(solution, 'power')  # noqa: WPS421
    assert hasattr(solution, 'sqrt')  # noqa: WPS421
    assert hasattr(solution, 'sub')  # noqa: WPS421


def test_references():
    assert solution.add is numbers2.add2
    assert solution.mul is numbers1.mul1
    assert solution.power is numbers2.power2
    assert solution.sqrt is numbers3.sqrt3
    assert solution.sub is numbers2.sub2


def test_all_metavar():
    assert 'add' in solution.__all__  # noqa: WPS609
    assert 'mul' in solution.__all__  # noqa: WPS609
    assert 'power' in solution.__all__  # noqa: WPS609
    assert 'sqrt' in solution.__all__  # noqa: WPS609
    assert 'sub' in solution.__all__  # noqa: WPS609


def main():
    test_names()
    test_references()
    test_all_metavar()


if __name__ == '__main__':
    main()
