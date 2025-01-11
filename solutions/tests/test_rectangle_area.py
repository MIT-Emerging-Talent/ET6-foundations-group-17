"""
Unit tests for the calculate_area function in rectangle_area.py
"""
import unittest
import sys
from pathlib import Path

# Ensure the `solutions` directory is in the Python path
sys.path.append(str(Path(__file__).parent.parent))
from rectangle_area import calculate_area


class TestRectangleArea(unittest.TestCase):
    """
    Test class for calculate_area function.
    """

    def test_positive_values(self):
        """Tests the function with positive values for length and width."""
        self.assertEqual(calculate_area(5.0, 3.0), 15.0)
        self.assertEqual(calculate_area(7.0, 2.5), 17.5)

    def test_zero_values(self):
        """Tests the function with zero values for length and width."""
        self.assertEqual(calculate_area(0.0, 5.0), 0.0)
        self.assertEqual(calculate_area(0.0, 0.0), 0.0)

    def test_negative_values(self):
        """Tests the function with negative values for length or width."""
        with self.assertRaises(ValueError) as context:
            calculate_area(-2.0, 3.0)
        self.assertEqual(
            str(context.exception),
            "Length and width must be positive numbers.",
        )


if __name__ == "__main__":
    unittest.main()
