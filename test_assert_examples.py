from string_calculator import StringCalculator

def test_add_empty ():
    assert StringCalculator.Add("") == 0
def test_add_single_number ():
    assert StringCalculator.Add("4") == 4
def test_add_two_numbers ():
    assert StringCalculator.Add("1,2") == 3
def test_add_many_numbers ():
    assert StringCalculator.Add("1,2,3,4,5,6,7,8,9,10") == 55
def test_add_newlines_separator ():
    assert StringCalculator.Add("1\n2,3")
def test_add_custom_separator():
    assert StringCalculator.Add("//;1\n2;3") == 6