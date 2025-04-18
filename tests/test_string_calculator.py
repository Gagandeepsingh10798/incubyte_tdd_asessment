from calculator.string_calculator import StringCalculator

def test_empty_string_returns_zero():
    calculator = StringCalculator()
    assert calculator.add("") == 0