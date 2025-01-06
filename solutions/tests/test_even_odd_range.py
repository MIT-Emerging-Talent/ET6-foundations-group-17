import unittest

from ..even_odd import even_odd_range


class TestEvenOddRange(unittest.TestCase):
    """
    Test case for the even_odd_range function.
    """

    def test_even_odd_range_valid(self):
        """
        Tests that the function correctly splits a range into even and odd numbers.
        """
        result = even_odd_range(1, 5)
        self.assertEqual(result, ([2, 4], [1, 3, 5]))

    def test_even_odd_range_empty(self):
        """
        Tests that an empty range returns two empty lists.
        """
        result = even_odd_range(5, 4)
        self.assertEqual(result, ([], []))

    def test_even_odd_range_single(self):
        """
        Tests that a single number in the range is classified correctly.
        """
        result = even_odd_range(4, 4)
        self.assertEqual(result, ([4], []))

    def test_even_odd_range_invalid_type(self):
        """
        Tests that ValueError is raised if start or end are not integers.
        """
        with self.assertRaises(ValueError):
            even_odd_range(1, "5")

    def test_even_odd_range_invalid_order(self):
        """
        Tests that ValueError is raised if start is greater than end.
        """
        with self.assertRaises(ValueError):
            even_odd_range(5, 3)
