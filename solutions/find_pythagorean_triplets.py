"""
This module finds all Pythagorean triplets (a, b, c) such that a^2 + b^2 = c^2
within a given range. It also supports finding primitive Pythagorean triplets.

Contents:
- `gcd`: Function to calculate the greatest common divisor of two integers.
- `find_primitive_pythagorean_triplets`: Function to find all primitive Pythagorean
    triplets within a given range.

Author: Malak Battatt
Date: January 8th, 2025
"""

from typing import List, Tuple


def gcd(x: int, y: int) -> int:
    """
    Calculate the greatest common divisor of x and y using the Euclidean algorithm.

    Args:
        x (int): The first integer
        y (int): The second integer

    Returns:
        int: The greatest common divisor of x and y

    Examples:
    >>> gcd(48, 18)
    6
    >>> gcd(56, 98)
    14
    """
    while y:
        x, y = y, x % y  # Update x and y to proceed with the Euclidean algorithm
    return x


def find_primitive_pythagorean_triplets(n: int) -> List[Tuple[int, int, int]]:
    """
    Find all primitive Pythagorean triplets (a, b, c) within the range [1, n].

    Args:
        n (int): The upper limit of the range to find triplets

    Returns:
        List[Tuple[int, int, int]]: A list of tuples representing primitive Pythagorean triplets

    Raises:
        ValueError: If n is not a positive integer

    Examples:
        >>> find_primitive_pythagorean_triplets(1)
        []
        >>> find_primitive_pythagorean_triplets(10)
        [(3, 4, 5)]
        >>> find_primitive_pythagorean_triplets(20)
        [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
        >>> find_primitive_pythagorean_triplets(50)
        [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The range must be a positive integer")

    triplets = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c_squared = a**2 + b**2
            c = int(c_squared**0.5)
            if c**2 == c_squared and c <= n:
                if gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) == 1:
                    triplets.append((a, b, c))
    return triplets
