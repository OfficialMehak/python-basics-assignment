import pytest
from starter_code.assignment import add_numbers, is_palindrome, find_max

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("RaceCar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True

def test_find_max():
    assert find_max([1, 2, 3]) == 3
    assert find_max([-5, -2, -10]) == -2
    assert find_max([7]) == 7
    assert find_max([100, 50, 200, 150]) == 200
