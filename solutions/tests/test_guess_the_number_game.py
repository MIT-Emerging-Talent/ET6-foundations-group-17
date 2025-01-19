"""
Unit test module for the Guess the Number game.
Contains tests for the random number generator and guessing logic.
Created on 11-01-25
@author: Ameen Agha
"""
import sys
import os
import unittest


# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Now import the function
from solutions.guess_the_number_game import generate_random_number, guess_the_number


class TestGuessTheNumber(unittest.TestCase):
    """
    Test cases for the Guess the Number game functions.
    These tests ensure random number generation and guessing logic
    work as expected.
    """

    def test_random_number_generation(self):
        """Test random number generation within a valid range."""
        random_numbers = [generate_random_number(1, 10) for _ in range(100)]
        self.assertTrue(all(1 <= num <= 10 for num in random_numbers))

    def test_random_number_invalid_range(self):
        """Test random number generation with invalid range."""
        with self.assertRaises(AssertionError):
            generate_random_number(10, 1)

    def test_random_number_non_integer_input(self):
        """Test random number generation with non-integer inputs."""
        with self.assertRaises(AssertionError):
            generate_random_number(1.5, 10)

    def test_guess_too_low(self):
        """Test guessing too low."""
        feedback = guess_the_number(10, 5)
        self.assertEqual(feedback, "Too low!")

    def test_guess_too_high(self):
        """Test guessing too high."""
        feedback = guess_the_number(10, 15)
        self.assertEqual(feedback, "Too high!")

    def test_guess_correct(self):
        """Test guessing correctly."""
        feedback = guess_the_number(10, 10)
        self.assertEqual(feedback, "Correct!")

    def test_guess_invalid_inputs(self):
        """Test guessing with non-integer inputs."""
        with self.assertRaises(AssertionError):
            guess_the_number(10, "five")


if __name__ == "__main__":
    unittest.main()
