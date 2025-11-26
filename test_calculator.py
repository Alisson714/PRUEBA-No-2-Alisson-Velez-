import pytest
from calculator import Calculator

def test_add_positive_numbers():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_add_negative_numbers():
    calc = Calculator()
    assert calc.add(-1, -1) == -2

def test_add_zero():
    calc = Calculator()
    assert calc.add(0, 5) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 3) == 7

def test_multiply():
    calc = Calculator()
    assert calc.multiply(4, 5) == 20

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        calc.divide(10, 0)
