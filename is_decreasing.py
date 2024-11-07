# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/06/2024
# Description: Write a recursive function named is_decreasing that takes as its parameter a list of numbers.
def is_decreasing(numbers):
    """
    This function checks if the given numbers are decreasing.
    """
    if len(numbers) == 2:
        return numbers[0] > numbers[1]

    # Check if the first 2 elements are in decreasing order
    if numbers[0] <= numbers[1]:
        return False

    # Recursive call to check the rest of the list.
    return is_decreasing(numbers[1:])
