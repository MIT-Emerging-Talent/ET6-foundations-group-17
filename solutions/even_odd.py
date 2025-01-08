"""
Returns two lists: even and odd numbers from the specified range.

The strategy is to iterate through the range (start to end, inclusive)
and check each number. If it's divisible by 2, it's even; otherwise, it's odd.

Arguments:
    start (int): The starting value of the range.
    end (int): The ending value of the range.

Returns:
    tuple: A tuple of two lists (even numbers, odd numbers).

Raises:
    ValueError: If start is greater than end.
    ValueError: If either start or end is not an integer.

Examples:
    >>> even_odd_range(1, 5)
    ([2, 4], [1, 3, 5])
    >>> even_odd_range(0, 0)
    ([0], [])
    >>> even_odd_range(5, 3)
    Traceback (most recent call last):
        ...
    ValueError: The start value must not be greater than the end value.
"""

from typing import List, Tuple


def even_odd_range(start: int, end: int) -> Tuple[List[int], List[int]]:
    """
    Returns two lists: one with the even numbers and one with the odd numbers
    within the specified range.

    Arguments:
    start -- The starting number (inclusive)
    end -- The ending number (inclusive)

    Returns:
    A tuple of two lists: the first list contains even numbers, the second contains odd numbers.
    """

    # Defensive assertions
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers.")
    if start > end:
        raise ValueError("The start value must not be greater than the end value.")

    even_numbers = []
    odd_numbers = []

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers
