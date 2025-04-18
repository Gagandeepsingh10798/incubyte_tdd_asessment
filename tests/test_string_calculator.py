from calculator.string_calculator import StringCalculator

def test_empty_string_returns_zero():
    calculator = StringCalculator()
    assert calculator.add("") == 0

def test_single_number_returns_value():
    calculator = StringCalculator()
    assert calculator.add("5") == 5