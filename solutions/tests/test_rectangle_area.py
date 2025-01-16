"""
Test module for rectangle_area.py

This module contains unit tests for the calculate_area function that validates:
- Calculations with positive numbers
- Handling of zero values
- Error handling for negative inputs

Each test function focuses on a single test case to ensure clear failure identification
and maintain test isolation.

Classes:
    TestRectangleArea: Collection of test cases for the calculate_area function
"""

import unittest
import sys
from pathlib import Path

# Add the parent directory to the system path to import rectangle_area
sys.path.append(str(Path(__file__).parent.parent))
from rectangle_area import calculate_area


class TestRectangleArea(unittest.TestCase):
    """
    Test cases for the calculate_area function.
    """

    def test_positive_values_case1(self):
        """Test with first set of positive values."""
        self.assertEqual(calculate_area(5.0, 3.0), 15.0)

    def test_positive_values_case2(self):
        """Test with second set of positive values."""
        self.assertEqual(calculate_area(10.0, 2.5), 25.0)

    def test_zero_length(self):
        """Test with zero length."""
        self.assertEqual(calculate_area(0.0, 5.0), 0.0)

    def test_zero_width(self):
        """Test with zero width."""
        self.assertEqual(calculate_area(5.0, 0.0), 0.0)

    def test_negative_length(self):
        """Test with negative length."""
        with self.assertRaises(ValueError) as context:
            calculate_area(-2.0, 3.0)
        self.assertEqual(
            str(context.exception), "Length and width must be positive numbers."
        )

    def test_negative_width(self):
        """Test with negative width."""
        with self.assertRaises(ValueError) as context:
            calculate_area(2.0, -3.0)
        self.assertEqual(
            str(context.exception), "Length and width must be positive numbers."
        )


if __name__ == "__main__":
    unittest.main()
