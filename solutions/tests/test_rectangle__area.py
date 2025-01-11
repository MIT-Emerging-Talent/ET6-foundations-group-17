"""
Unit tests for the calculate_area function in rectangle_area.py
"""
import unittest
import sys
from pathlib import Path

# Add the parent directory to the system path to import rectangle_area
sys.path.append(str(Path(__file__).parent.parent))
from rectangle_area import calculate_area


class TestRectangleArea(unittest.TestCase):
    """
    Test class for calculate_area function.
    """

    def test_positive_values(self):
        """
        Tests the function with positive values for length and width.
        """
        length = 5.0
        width = 3.0
        expected_area = 15.0

        actual_area = calculate_area(length, width)
        self.assertEqual(actual_area, expected_area, "Incorrect calculation for positive values.")

    def test_zero_values(self):
        """
        Tests the function with zero values for length and width (boundary case).
        """
        length = 0.0
        width = 5.0
        expected_area = 0.0

        actual_area = calculate_area(length, width)
        self.assertEqual(actual_area, expected_area, "Incorrect calculation for zero values.")

    def test_negative_values(self):
        """
        Tests the function with negative values for length or width (defensive assertion).
        """
        with self.assertRaises(ValueError) as context:
            calculate_area(-2.0, 3.0)
        self.assertEqual(
            str(context.exception),
            "Length and width must be positive numbers.",
            "Incorrect error message for negative values.",
        )


if __name__ == "__main__":
    unittest.main()