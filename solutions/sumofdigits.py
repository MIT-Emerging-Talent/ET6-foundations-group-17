
"""
A module for calculating the sum of digits of an integer.

Module contents:
    - sum_of_digits: calculates the sum of the digits of an integer.

Created on 07-01-25
@author: Panashe Matarutse
"""


def sum_of_digits(n: int) -> int:
    """
    Calculate the sum of the digits of a given integer.

    Parameters:
        n: the integer whose digits will be summed.

    Returns:
        int: the sum of the digits of the integer.

    Raises:
        AssertionError: if the input is not an integer.

    Examples:
        >>> sum_of_digits(1234)
        10
        >>> sum_of_digits(987)
        24
        >>> sum_of_digits(-456)
        15
        >>> sum_of_digits(0)
        0
    """
    assert isinstance(n, int), "Input must be an integer."

    # Handle negative integers by taking the absolute value
    n = abs(n)

    # Convert the integer to a string, iterate over its characters, convert each back to an integer, and sum them
    return sum(int(digit) for digit in str(n))

