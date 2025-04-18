import pytest
from calculator.string_calculator import StringCalculator

def test_empty_string_returns_zero():
    calculator = StringCalculator()
    assert calculator.add("") == 0

def test_single_number_returns_value():
    calculator = StringCalculator()
    assert calculator.add("5") == 5

def test_two_numbers_returns_sum():
    calculator = StringCalculator()
    assert calculator.add("1,2") == 3

def test_multiple_numbers_returns_sum():
    calculator = StringCalculator()
    assert calculator.add("1,2,3,4") == 10

def test_newline_as_delimiter():
    calculator = StringCalculator()
    assert calculator.add("1\n2,3") == 6

def test_custom_delimiter():
    calculator = StringCalculator()
    assert calculator.add("//;\n1;2") == 3

def test_negative_numbers_raise_exception():
    calculator = StringCalculator()
    with pytest.raises(ValueError) as excinfo:
        calculator.add("1,-2,3,-4")
    assert str(excinfo.value) == "negative numbers not allowed -2,-4"

def test_delimiter_of_any_length():
    calculator = StringCalculator()
    assert calculator.add("//[***]\n1***2***3") == 6

def test_multiple_delimiters():
    calculator = StringCalculator()
    assert calculator.add("//[*][%]\n1*2%3") == 6

def test_multiple_delimiters_of_different_lengths():
    calculator = StringCalculator()
    assert calculator.add("//[***][%%]\n1***2%%3") == 6