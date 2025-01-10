import unittest
from rectangle_area import calculate_area  # Import the function you're testing


class TestRectangleArea(unittest.TestCase):
    def test_zero_values(self):
        # Test with zero values
        length = 0.0
        width = 5.0
        expected_area = 0.0
        actual_area = calculate_area(length, width)
        self.assertEqual(
            actual_area, expected_area, "Incorrect calculation for zero values."
        )

    def test_negative_values(self):
        # Test with negative values
        try:
            calculate_area(-2.0, 3.0)
        except ValueError as e:
            self.assertEqual(
                str(e),
                "Length and width must be positive numbers.",
                "Incorrect error message for negative values.",
            )
        else:
            self.fail("ValueError not raised for negative input.")
