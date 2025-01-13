import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from chocolate_distribution import minimize_chocolate_difference


class TestMinimizeChocolateDifference(unittest.TestCase):
    def test_valid_case(self):
        """Test a valid case with enough packets and students."""
        chocolates = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
        k = 7
        result = minimize_chocolate_difference(chocolates, k)
        self.assertEqual(result, 10)

    def test_not_enough_packets(self):
        """Test the case where there are fewer packets than students."""
        chocolates = [1, 2, 3]
        k = 5
        result = minimize_chocolate_difference(chocolates, k)
        self.assertEqual(result, -1)

    def test_empty_chocolates_list(self):
        """Test the case where the chocolates list is empty."""
        chocolates = []
        k = 3
        result = minimize_chocolate_difference(chocolates, k)
        self.assertEqual(result, 0)

    def test_zero_students(self):
        """Test the case where the number of students is zero."""
        chocolates = [10, 20, 30]
        k = 0
        result = minimize_chocolate_difference(chocolates, k)
        self.assertEqual(result, 0)

    def test_single_packet(self):
        """Test the case with only one packet and one student."""
        chocolates = [42]
        k = 1
        result = minimize_chocolate_difference(chocolates, k)
        self.assertEqual(result, 0)

    def test_minimized_difference(self):
        """Test a generic case to validate the minimized difference calculation."""
        chocolates = [7, 3, 2, 4, 9, 12, 56]
        k = 3
        result = minimize_chocolate_difference(chocolates, k)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
