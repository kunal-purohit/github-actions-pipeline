import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-1, 3) == -3

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
