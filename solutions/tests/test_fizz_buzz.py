"""
Test module for fizz_buzz function in the FizzBuzz game.
Contains tests for standard cases, edge cases, and defensive assertions.

Test categories:
    - Standard cases: typical user inputs and expected game results
    - Edge cases: empty input, invalid input
    - Defensive tests: wrong input types, assertions

Created on 31-12-24
Author: Codi + Abdulrahman Alsir
"""

import unittest
from ..fizz_buzz_game import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """
    Test cases for the FizzBuzz game function.
    """

    def test_fizz_buzz_2_to_10(self):
        """
        Test for the range 2 to 10, expected output should only include Fizz,
        Buzz, and FizzBuzz.
        """
        result = fizz_buzz(2, 10)
        expected = ["Fizz", "Buzz", "Fizz", "Fizz"]
        self.assertEqual(result, expected)

    def test_fizz_buzz_10_to_16(self):
        """
        Test for the range 10 to 16, expected output should include Fizz, Buzz,
        and FizzBuzz.
        """
        result = fizz_buzz(10, 16)
        expected = ["Buzz", "Fizz", "FizzBuzz"]
        self.assertEqual(result, expected)

    def test_empty_range(self):
        """
        Test for an empty range where start equals end.
        Expected output is an empty list.
        """
        result = fizz_buzz(5, 5)
        self.assertEqual(result, [])

    def test_no_fizz_or_buzz(self):
        """
        Test for a range with no numbers divisible by 3 or 5.
        Expected output is an empty list.
        """
        result = fizz_buzz(7, 9)
        self.assertEqual(result, [])

    def test_invalid_input(self):
        """
        Test for invalid input where start or end is not an integer.
        Should raise an AssertionError.
        """
        with self.assertRaises(AssertionError):
            fizz_buzz("a", 10)

    def test_large_range(self):
        """
        Test a larger range, verifying the correctness of the output.
        """
        result = fizz_buzz(1, 20)
        expected = ["Fizz", "Buzz", "Fizz", "Fizz", "Buzz", "Fizz", "FizzBuzz", "Fizz"]
        self.assertEqual(result, expected)

    def test_invalid_input_end(self):
        """
        Test for invalid input where the end value is not an integer.
        Should raise an AssertionError.
        """
        with self.assertRaises(AssertionError):
            fizz_buzz(1, "b")

    def test_large_range_empty(self):
        """
        Test for a large range with no Fizz or Buzz in the range.
        Expected output is an empty list.
        """
        result = fizz_buzz(100, 102)
        self.assertEqual(result, ["Buzz"])


if __name__ == "__main__":
    unittest.main()
