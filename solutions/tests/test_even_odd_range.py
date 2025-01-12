"""
Unit tests for the even_odd_range function.

This test file includes:
- Tests for valid ranges (including single numbers).
- Tests for edge cases like negative numbers.
- Tests for invalid inputs like non-integer types.
- Tests for large ranges.
"""

import unittest

try:
    # For package execution
    from ..even_odd import even_odd_range
except ImportError:
    # For standalone execution
    from even_odd import even_odd_range


class TestEvenOddRange(unittest.TestCase):
    """
    Test case for the even_odd_range function.
    """

    def test_even_odd_range_valid(self):
        """Tests valid ranges with both even and odd numbers."""
        result = even_odd_range(1, 5)
        self.assertEqual(result, ([2, 4], [1, 3, 5]))

    def test_even_odd_range_single(self):
        """Tests single number in the range (even)."""
        result = even_odd_range(4, 4)
        self.assertEqual(result, ([4], []))

    def test_even_odd_range_negative_numbers(self):
        """Tests ranges that include negative numbers."""
        result = even_odd_range(-5, 0)
        self.assertEqual(result, ([-4, -2, 0], [-5, -3, -1]))

    def test_even_odd_range_large_range(self):
        """Tests large ranges."""
        result = even_odd_range(1, 100)
        self.assertEqual(result[0], list(range(2, 101, 2)))
        self.assertEqual(result[1], list(range(1, 101, 2)))

    def test_even_odd_range_invalid_type(self):
        """Tests ValueError for non-integer inputs."""
        with self.assertRaises(ValueError):
            even_odd_range(1, "5")

    def test_even_odd_range_invalid_order(self):
        """Tests ValueError when start > end."""
        with self.assertRaises(ValueError):
            even_odd_range(5, 3)


if __name__ == "__main__":
    unittest.main()
