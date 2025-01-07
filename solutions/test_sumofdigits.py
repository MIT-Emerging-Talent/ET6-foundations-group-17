"""
Test module for sum_of_digits function.
Contains tests for standard cases, edge cases, and defensive assertions.
Test categories:
    - Standard cases: typical user inputs and expected results
    - Edge cases: single-digit numbers, zero, and negative numbers
    - Defensive tests: wrong input types, assertions
Created on 07-01-25
Author: Panashe Matarutse
"""

import unittest
from sumofdigits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    """
    Test cases for the sum_of_digits function.
    """

    def test_standard_case_positive_number(self):
        """
        Test for a standard positive number.
        Expected result is the sum of its digits.
        """
        result = sum_of_digits(1234)
        self.assertEqual(result, 10)

    def test_standard_case_another_positive_number(self):
        """
        Test for another standard positive number.
        Expected result is the sum of its digits.
        """
        result = sum_of_digits(987)
        self.assertEqual(result, 24)

    def test_edge_case_single_digit(self):
        """
        Test for a single-digit number.
        Expected result is the number itself.
        """
        result = sum_of_digits(5)
        self.assertEqual(result, 5)

    def test_edge_case_zero(self):
        """
        Test for zero as input.
        Expected result is zero.
        """
        result = sum_of_digits(0)
        self.assertEqual(result, 0)

    def test_edge_case_negative_number(self):
        """
        Test for a negative number.
        Expected result is the sum of the absolute value's digits.
        """
        result = sum_of_digits(-1234)
        self.assertEqual(result, 10)

    def test_large_number(self):
        """
        Test for a large positive number.
        Expected result is the sum of its digits.
        """
        result = sum_of_digits(987654321)
        self.assertEqual(result, 45)

    def test_defensive_non_integer_input(self):
        """
        Test for a non-integer input.
        Expected result is an AssertionError.
        """
        with self.assertRaises(AssertionError):
            sum_of_digits("1234")  # Passing a string instead of an integer


if __name__ == "__main__":
    unittest.main()
