# from calculator import sum
from string_calculator import StringCalculator

# def test_uppercase():
#     assert "loud noises".upper() == "LOUD NOISES"

# def test_reversed():
#     assert list (reversed([1,2,3,4])) == [4,3,2,1]

# def test_some_primes():
#     assert 37 in {
#         num 
#         for num in range(2,50)
#         if not any(num % div ==0 for div in range(2,num))
#     }

# # def test_sum ():
# #     assert sum("a",3)

def test_add_empty ():
    assert StringCalculator.Add("") == 0
def test_add_single_number ():
    assert StringCalculator.Add("4") == 4
def test_add_two_number ():
    assert StringCalculator.Add("1,2") == 3
