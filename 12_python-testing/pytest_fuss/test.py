import pytest
from library import sqr


def test_sqr():
    assert sqr(1) == 1
    assert sqr(-1) == 1
    assert sqr(9) == 81
    assert sqr(9) == 80