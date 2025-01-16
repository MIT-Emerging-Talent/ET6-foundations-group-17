import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(file).parent.parent))
from even_odd_range import even_odd_range


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

    def test_even_odd_range_large_range_even(self):
        """Tests large range for even numbers."""
        result = even_odd_range(1, 100)
        self.assertEqual(result[0], list(range(2, 101, 2)))

    def test_even_odd_range_large_range_odd(self):
        """Tests large range for odd numbers."""
        result = even_odd_range(1, 100)
        self.assertEqual(result[1], list(range(1, 101, 2)))

    def test_even_odd_range_invalid_type(self):
        """Tests ValueError for non-integer inputs."""
        with self.assertRaises(ValueError) as context:
            even_odd_range(1, "5")
        self.assertEqual(str(context.exception), "Both start and end must be integers.")

    def test_even_odd_range_invalid_order(self):
        """Tests ValueError when start > end."""
        with self.assertRaises(ValueError) as context:
            even_odd_range(5, 3)
        self.assertEqual(str(context.exception), "The start value must not be greater than the end value.")

    def test_even_odd_range_empty_range(self):
        """Tests empty range with the same start and end."""
        result = even_odd_range(5, 5)
        self.assertEqual(result, ([], [5]))

    def test_even_odd_range_all_negative(self):
        """Tests range with only negative numbers."""
        result = even_odd_range(-10, -1)
        self.assertEqual(result, ([-10, -8, -6, -4, -2], [-9, -7, -5, -3, -1]))

if _name_ == "_main_":
    unittest.main()
