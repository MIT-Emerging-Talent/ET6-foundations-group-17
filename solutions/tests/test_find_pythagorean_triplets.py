"""
Unit tests for the find_pythagorean_triplets module.

This module contains unit tests for the number guessing game, specifically testing
the find_primitive_pythagorean_triplets function.

Tests included:
- TestFindPrimitivePythagoreanTriplets: Tests for the find_primitive_pythagorean_triplets function.

Author: Malak Battatt
Date: January 8th, 2025
"""

import os
import sys
import unittest

from ..find_pythagorean_triplets import find_primitive_pythagorean_triplets

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestFindPrimitivePythagoreanTriplets(unittest.TestCase):
    """Unit tests for the `find_primitive_pythagorean_triplets` function."""

    def test_valid_range(self):
        """Test with a valid range value"""
        self.assertEqual(find_primitive_pythagorean_triplets(10), [(3, 4, 5)])

    def test_multiple_triplets(self):
        """Test with a range that includes multiple triplets"""
        self.assertEqual(
            find_primitive_pythagorean_triplets(20),
            [(3, 4, 5), (5, 12, 13), (8, 15, 17)],
        )

    def test_no_triplets(self):
        """Test with a range that includes no triplets"""
        self.assertEqual(find_primitive_pythagorean_triplets(2), [])

    def test_invalid_range_type(self):
        """Test with an invalid range type"""
        with self.assertRaises(ValueError):
            find_primitive_pythagorean_triplets("not a number")

    def test_negative_range(self):
        """Test with a negative range value"""
        with self.assertRaises(ValueError):
            find_primitive_pythagorean_triplets(-5)

    def test_large_input(self):
        """Test with a very large range value to ensure performance"""
        result = find_primitive_pythagorean_triplets(
            10**6
        )  # Added test for large input
        # Checking the length to ensure it runs and returns results
        self.assertTrue(len(result) > 0)


if __name__ == "__main__":
    unittest.main()
