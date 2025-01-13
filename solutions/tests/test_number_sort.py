"""
Test module for the sort function in the custom Bubble Sort implementation.
Contains tests for standard cases, edge cases, and defensive assertions.

Test categories:
    - Standard cases: typical lists of numbers to verify sorting correctness
    - Edge cases: empty lists, single-element lists, duplicate values
    - Defensive tests: invalid input types, assertions

Created on 03-01-25
Updated on 10-01-25
Author: Cody (Reviewed By Abdulrahman)
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from number_sort import sort


class TestBubbleSort(unittest.TestCase):
    """
    Test cases for the custom Bubble Sort function.
    """

    def test_standard_case(self):
        """Test for a typical list of unsorted numbers."""
        result = sort([4, 2, 7, 1, 9, 5])
        expected = [1, 2, 4, 5, 7, 9]
        self.assertEqual(result, expected)

    def test_reverse_order(self):
        """Test for a list in reverse order."""
        result = sort([10, 9, 8, 7, 6, 5])
        expected = [5, 6, 7, 8, 9, 10]
        self.assertEqual(result, expected)

    def test_sorted_input(self):
        """Test for a list that is already sorted."""
        result = sort([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_single_element(self):
        """Test for a list with a single element."""
        result = sort([42])
        expected = [42]
        self.assertEqual(result, expected)

    def test_empty_list(self):
        """Test for an empty list."""
        result = sort([])
        expected = []
        self.assertEqual(result, expected)

    def test_duplicates(self):
        """Test for a list with duplicate numbers."""
        result = sort([4, 2, 7, 2, 5, 4])
        expected = [2, 2, 4, 4, 5, 7]
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Test for a list with negative numbers."""
        result = sort([-3, -1, -4, -2])
        expected = [-4, -3, -2, -1]
        self.assertEqual(result, expected)

    def test_mixed_numbers(self):
        """Test for a list with a mix of positive and negative numbers."""
        result = sort([-2, 3, 0, -1, 4])
        expected = [-2, -1, 0, 3, 4]
        self.assertEqual(result, expected)

    def test_invalid_input_type(self):
        """Test for invalid input where the argument is not a list."""
        with self.assertRaises(TypeError):
            sort("not_a_list")

    def test_non_numeric_elements(self):
        """Test for a list with non-numeric elements."""
        with self.assertRaises(ValueError):
            sort([1, "a", 3])

    def test_large_numbers(self):
        """Test for lists with very large numbers."""
        result = sort([10**6, -(10**6), 0])
        expected = [-(10**6), 0, 10**6]
        self.assertEqual(result, expected)

    def test_very_large_numbers(self):
        """Test sorting numbers in the millions range."""
        result = sort([2000000, 1000000, 3000000])
        expected = [1000000, 2000000, 3000000]
        self.assertEqual(result, expected)

    def test_very_small_numbers(self):
        """Test sorting very small decimal numbers."""
        result = sort([0.0001, 0.0003, 0.0002])
        expected = [0.0001, 0.0002, 0.0003]
        self.assertEqual(result, expected)

    def test_wide_range_numbers(self):
        """Test sorting numbers with very different magnitudes."""
        result = sort([1000000, 0.001, 1, 10000])
        expected = [0.001, 1, 10000, 1000000]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
