import unittest

import sys
from pathlib import Path
sys.path.append(str(Path(file).parent.parent))
from even_odd_range import even_odd_range
import unittest



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
        with self.assertRaises(ValueError):
            even_odd_range(1, "5")

    def test_even_odd_range_invalid_order(self):
        """Tests ValueError when start > end."""
        with self.assertRaises(ValueError):
            even_odd_range(5, 3)


if __name__ == "__main__":
    unittest.main()
