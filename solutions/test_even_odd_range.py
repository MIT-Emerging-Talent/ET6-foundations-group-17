"""
Unit tests for the even_odd_range function.

This test file includes:
- Basic functionality tests.
- Tests for edge cases (e.g., empty ranges, single numbers).
- Tests for defensive assertions (e.g., invalid inputs).
- Tests for large ranges and negative numbers.
"""

import unittest

from ..even_odd import even_odd_range


class TestEvenOddRange(unittest.TestCase):
    """
    Test case for the even_odd_range function.
    """

    def test_even_odd_range_valid(self):
        """
        Tests that the function correctly splits a range into even and odd numbers.
        """
        result = even_odd_range(1, 5)
        self.assertEqual(result, ([2, 4], [1, 3, 5]))

    def test_even_odd_range_single(self):
        """
        Tests that a single number in the range is classified correctly.
        """
        result = even_odd_range(4, 4)
        self.assertEqual(result, ([4], []))

    def test_even_odd_range_invalid_type(self):
        """
        Tests that ValueError is raised if start or end are not integers.
        """
        with self.assertRaises(ValueError):
            even_odd_range(1, "5")

    def test_even_odd_range_invalid_order(self):
        """
        Tests that ValueError is raised if start is greater than end.
        """
        with self.assertRaises(ValueError):
            even_odd_range(5, 3)
def test_even_odd_range_negative_numbers(self):
    """
    Tests the function with a range that includes negative numbers.
    """
    result = even_odd_range(-5, 0)
    self.assertEqual(result, ([0, -4], [-5, -3, -1]))

def test_even_odd_range_large_range(self):
    """
    Tests the function with a large range.
    """
    result = even_odd_range(1, 100)
    self.assertEqual(result[0], list(range(2, 101, 2)))  # Even numbers
    self.assertEqual(result[1], list(range(1, 101, 2)))  # Odd numbers
