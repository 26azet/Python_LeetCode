import pytest
from solution import Solution
from classes.singly_list_node import SinglyListNode
from classes.singly_list_of_digits import SinglyListOfDigits

def test_singly_list_of_digits_init_and_str():
    l = SinglyListOfDigits([1, 2, 3])
    assert l.to_list() == [1, 2, 3]

def test_singly_list_of_digits_append():
    l = SinglyListOfDigits([4])
    l.append([5])
    l.append([6])
    assert l.to_list() == [4, 5, 6]

def test_add_two_numbers_simple():
    l1 = SinglyListOfDigits([2, 4, 3])
    l2 = SinglyListOfDigits([5, 6, 4])
    solution = Solution()
    result = solution.add_two_numbers(l1, l2)
    assert result.to_list() == [7, 0, 8]

def test_add_two_numbers_with_carry():
    l1 = SinglyListOfDigits([9, 9, 9])
    l2 = SinglyListOfDigits([1])
    solution = Solution()
    result = solution.add_two_numbers(l1, l2)
    assert result.to_list() == [0, 0, 0, 1]

def test_add_two_numbers_different_lengths():
    l1 = SinglyListOfDigits([1, 8])
    l2 = SinglyListOfDigits([0])
    solution = Solution()
    result = solution.add_two_numbers(l1, l2)
    assert result.to_list() == [1, 8]

def test_add_two_numbers_empty_lists():
    l1 = SinglyListOfDigits([])
    l2 = SinglyListOfDigits([])
    solution = Solution()
    result = solution.add_two_numbers(l1, l2)
    assert result.to_list() == []

def test_add_two_numbers_example_from_file():
    l1 = SinglyListOfDigits([2,2,3,4,5,6])
    l2 = SinglyListOfDigits([5,6,4,3,2,1])
    solution = Solution()
    result = solution.add_two_numbers(l1, l2)
    
    assert result.to_list() == [7, 8, 7, 7, 7, 7]

def test_digit_value_error():
    with pytest.raises(ValueError):
        SinglyListNode(10)  # Should raise ValueError for digit > 9
    with pytest.raises(ValueError):
        SinglyListNode(-1)  # Should raise ValueError for digit < 0
    with pytest.raises(ValueError):
        SinglyListOfDigits([1,2,3,4,5,6,10])  # Should raise ValueError for digit > 9
    with pytest.raises(ValueError):
        list_of_digits = SinglyListOfDigits([1,2,3,4,5,6])
        list_of_digits.append([9,3,2,103423])
    