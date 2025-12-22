import pytest
from src.handlers.math import multiply, divide


def test_multiply_basic():
    assert multiply(6, 7) == 42


def test_multiply_float():
    assert multiply(2.5, 4) == 10.0


def test_multiply_negative():
    assert multiply(-3, 5) == -15


def test_divide_basic():
    assert divide(14, 4) == 3.5


def test_divide_float():
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
