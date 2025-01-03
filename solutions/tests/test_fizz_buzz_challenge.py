"""
Test module for fizz_buzz function in the FizzBuzz game.
Contains tests for standard cases, edge cases, and defensive assertions.

Test categories:
    - Standard cases: typical user inputs and expected game results
    - Edge cases: empty input, invalid input, and quitting the game
    - Defensive tests: wrong input types, assertions

Created on 31-12-24
Author: Codi + Abdulrahman Alsir
"""

import unittest
from ..fizz_buzz_challenge import fizz_buzz


class TestFizzBuzzChallenge(unittest.TestCase):
    """
    Test cases for the FizzBuzz Challenge function.

    These tests verify that the fizz_buzz_challenge function correctly
    identifies numbers divisible by 3, 5, or both, and returns the correct
    results based on the game rules.
    """

    def test_range_2_to_10(self):
        """
        Test for the range 2 to 10, expected output should include only Fizz,
        Buzz, and FizzBuzz.
        """
        result = fizz_buzz(2, 10)
        expected = {3: "Fizz", 5: "Buzz", 6: "Fizz", 9: "Fizz"}
        self.assertEqual(result, expected)

    def test_range_10_to_16(self):
        """
        Test for the range 10 to 16, expected output should include Fizz, Buzz,
        and FizzBuzz.
        """
        result = fizz_buzz(10, 16)
        expected = {10: "Buzz", 12: "Fizz", 15: "FizzBuzz"}
        self.assertEqual(result, expected)

    def test_empty_range(self):
        """
        Test for an empty range where start equals end. Expected output is an
        empty dictionary.
        """
        result = fizz_buzz(5, 5)
        self.assertEqual(result, {})

    def test_no_fizz_or_buzz(self):
        """
        Test for a range with no numbers divisible by 3 or 5. Expected output is
        an empty dictionary.
        """
        result = fizz_buzz(7, 9)
        self.assertEqual(result, {})

    def test_single_fizz(self):
        """
        Test for a range that contains only Fizz (divisible by 3 but not 5).
        """
        result = fizz_buzz(3, 4)
        expected = {3: "Fizz"}
        self.assertEqual(result, expected)

    def test_single_buzz(self):
        """
        Test for a range that contains only Buzz (divisible by 5 but not 3).
        """
        result = fizz_buzz(5, 6)
        expected = {5: "Buzz"}
        self.assertEqual(result, expected)

    def test_invalid_input_start(self):
        """
        Test for invalid input where start is not an integer.
        Should raise an AssertionError.
        """
        with self.assertRaises(AssertionError):
            fizz_buzz("a", 10)

    def test_invalid_input_end(self):
        """
        Test for invalid input where end is not an integer.
        Should raise an AssertionError.
        """
        with self.assertRaises(AssertionError):
            fizz_buzz(10, "b")

    def test_large_range(self):
        """
        Test a larger range, verifying the correctness of the output.
        """
        result = fizz_buzz(1, 20)
        expected = {
            3: "Fizz",
            5: "Buzz",
            6: "Fizz",
            9: "Fizz",
            10: "Buzz",
            12: "Fizz",
            15: "FizzBuzz",
            18: "Fizz",
        }
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
