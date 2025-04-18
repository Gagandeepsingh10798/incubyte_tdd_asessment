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