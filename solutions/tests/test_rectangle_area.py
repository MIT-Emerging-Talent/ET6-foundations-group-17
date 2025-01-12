"""
Unit tests for the calculate_area function in rectangle_area.py.
"""

import unittest
import sys
from pathlib import Path

# Add the parent directory to the system path to import rectangle_area
sys.path.append(str(Path(__file__).parent.parent))
from rectangle_area import calculate_area  # noqa: F401


class TestRectangleArea(unittest.TestCase):
    """
    Test cases for the calculate_area function.
    """

    def test_positive_values(self):
        """
        Test with positive values for length and width.
        """
        self.assertEqual(calculate_area(5.0, 3.0), 15.0)
        self.assertEqual(calculate_area(10.0, 2.5), 25.0)

    def test_zero_values(self):
        """
        Test with zero for length or width (boundary case).
        """
        self.assertEqual(calculate_area(0.0, 5.0), 0.0)
        self.assertEqual(calculate_area(5.0, 0.0), 0.0)

    def test_negative_values(self):
        """
        Test with negative values for length or width.
        """
        with self.assertRaises(ValueError) as context:
            calculate_area(-2.0, 3.0)
        self.assertEqual(
            str(context.exception), "Length and width must be positive numbers."
        )

        with self.assertRaises(ValueError) as context:
            calculate_area(2.0, -3.0)
        self.assertEqual(
            str(context.exception), "Length and width must be positive numbers."
        )


if __name__ == "__main__":
    unittest.main()
