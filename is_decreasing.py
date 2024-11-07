# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/06/2024
# Description: Write a recursive function named is_decreasing that takes as its parameter a list of numbers.
def is_decreasing(numbers):
    """
    This function checks if the given numbers are decreasing.
    """
    if len(numbers) < 2:
        raise ValueError

    def helper(index):
        """
        Helper function for recursive calls.
        """
        if index == len(numbers) - 1:
            return True
        return numbers[index] > numbers[index + 1] and helper(index + 1)
    return helper(0)